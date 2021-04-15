import pyshark
import subprocess
import sys
import os


class AudioPCAP(object):

    def __init__(self, pcap, outputfile):
        self.rawAudio = None
        self.rtpPackets = []
        self.pcap = pcap
        self.nameFile = outputfile
        self.extractRtpPayload()

    def extractRtpPayload(self):
        print("Trying to find RTP payload ...")
        pcap = pyshark.FileCapture(self.pcap, display_filter="rtp")
        for packet in pcap:
            try:
                rtpPacket = packet[3]
                if rtpPacket.payload:
                    self.rtpPackets.append(rtpPacket.payload.split(":"))
            except:
                pass
        if (len(self.rtpPackets) != 0 ):
            self.assembleRawAudio()
            self.convertRawToWav()
        else:
            print("Your .pcap does not have packets using RTP, no audio found !")
            

    def assembleRawAudio(self):
        print("Creating raw audio file ...")
        nameRaw = self.nameFile + ".raw"
        self.rawAudio = open(nameRaw,"wb")
        for rtpPacket in self.rtpPackets:
            joined = ''.join(rtpPacket)
            audioSample = bytearray.fromhex(joined)
            self.rawAudio.write(audioSample)
        self.rawAudio.close()

    def convertRawToWav(self):
        print("Converting to .wav ...")
        if self.rawAudio is not None:
            subprocess.run(f"sox -r 8000 -e u-law -b 8 -c 1 {self.nameFile}.raw {self.nameFile}.wav", shell=True)
            subprocess.run(f"rm {self.nameFile}.raw", shell=True)
        print(f"Completed process: the file {self.nameFile}.wav is in your working directory")

def checkArguments(arguments):
    if len(sys.argv)!=3:
        print( "Bad number of arguments, must be 2!")
        print( "First argument: a .pcap")
        print( "Second argument: name of output .wav file")
        exit()
    else:
        name, extensionPCAP = os.path.splitext(sys.argv[1])
        if extensionPCAP != '.pcap':
            print("First argument was not .pcap file !")
            print(f"Your first argument has {extensionPCAP} for extension")
            exit()
        else:
            nameOutputFile,extension = os.path.splitext(sys.argv[2])
            AudioPCAP(str(sys.argv[1]),nameOutputFile)


if __name__ == '__main__':
    checkArguments(sys.argv)
