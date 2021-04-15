from scapy.all import TCP, rdpcap
from collections import namedtuple
import os
import re

HTTPFrame = namedtuple('HTTPFrame', ['header', 'payload'])


def getHeaderPayload(payload):
    try:
        header_raw = payload[:payload.index(b'\r\n\r\n') + 2]
    except ValueError:
        return None
    # Content-Type: image/png\r\n
    header = dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n', header_raw.decode()))
    if 'Content-Type' not in header:
        return None
    return header


def extractImageContent(httpFrame):
    imageContent = None
    imageType = None
    if 'image' in httpFrame.header['Content-Type']:
        # httpFrame.header['Content-Type'] = image/extension
        imageType = httpFrame.header['Content-Type'].split('/')[1]
        imageContent = httpFrame.payload[httpFrame.payload.index(b'\r\n\r\n') + 4:]
    return imageContent, imageType


class ImagePCAP:
    def __init__(self, fname):
        pcap = rdpcap(fname)
        self.numberImages = 0
        self.sessions = pcap.sessions()
        self.httpFrameList = []
        self.getHTTPPayload()
        self.write()
        print(f"{self.numberImages} image(s) extracted")

    def getHTTPPayload(self):
        for session in self.sessions:
            payload = b''
            for packet in self.sessions[session]:
                try:
                    # HTTP port 80
                    if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                        payload += bytes(packet[TCP].payload)
                except IndexError:
                    pass
            if payload:
                header = getHeaderPayload(payload)
                if header is None:
                    continue
                frame = HTTPFrame(header, payload)
                self.httpFrameList.append(frame)

    def write(self):
        for httpFrame in self.httpFrameList:
            contentImage, extensionImage = extractImageContent(httpFrame)
            # None,None if no image in httpFrame
            if contentImage and extensionImage:
                newImageName = os.path.join("Model/ResultAttack/Results/Pictures",
                                            f'image_{self.numberImages}.{extensionImage}')
                self.numberImages += 1
                with open(newImageName, 'wb') as f:
                    f.write(contentImage)
