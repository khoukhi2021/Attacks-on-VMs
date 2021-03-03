import pyshark
import subprocess

class VoipCallAssembler(object):

    def __init__(self, pcap):
        self.rawAudio = None
        self.rtpStreams = []
        self.pcap = pcap
        self.extractRtpStreams()
        self.assembleRawAudio()
        self.convertRawToWav("test")

    def extractRtpStreams(self):
        capture = pyshark.FileCapture(self.pcap, display_filter="rtp")
        for packet in capture:
            try:
                rtpStream = packet[3]
                print(packet[3]) # information on payload type for better sox conversion
                if rtpStream.payload:
                    self.rtpStreams.append(rtpStream.payload.split(":"))
            except:
                pass

    def assembleRawAudio(self):
        self.rawAudio = open("test.raw","wb")
        for rtpStream in self.rtpStreams:
            joined = ''.join(rtpStream)
            audioSample = bytearray.fromhex(joined)
            self.rawAudio.write(audioSample)
        self.rawAudio.close()

    def convertRawToWav(self,nameFile):
        if self.rawAudio is not None:
            subprocess.call(f"sox -r 8000 -e u-law -b 8 -c 1 {nameFile}.raw {nameFile}.wav", shell=True)


if __name__ == '__main__':
    VoipCallAssembler("Forensic.pcap")
