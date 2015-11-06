import logging

class audioType （object):
    def __init__(self, filename):
        audioFile = filename
        audioFormat = ''
        audioRate = 0
        audioLanguage = ''
        minBlockSize = 0
        maxBlockSize = 0
        minFrameSize = 0
        maxFrameSize = 0
        sampleRate = 0
        channels = 0
        bitsperSample = 0
        length = 0
        
class flacType （object):
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__)
        audioFile = filename
        error = ''
    def getAttribute()
        with open(filename, 'rb') as file:
            bytes = file.read(4)  # get Magic Number
            if bytes != "fLaC":
                self.error += "Not a fLaC file! Aborting\n"
            bytes = file.read(1)  # Get STREAMINFO metadata Block Header
            if ord(bytes) == 0:  # "STREAMINFO BLOCK FOUND"
                audioInfo = audioType(audioFile)
                # Jump to the STREAMINFO Block, 24 bits from here.
                file.seek(3,1)
                # parse STREMINFO BLOCK
                audioInfo.minBlockSize, audioInfo.maxBlockSize = unpack('>HH', file.read(4))
                audioInfo.minFrameSize = unpack('>I', '\x00' + file.read(3))
                audioInfo.maxFrameSize = unpack('>I', '\x00' + file.read(3))
                if audioInfo.minBlockSize < 16 or audioInfo.maxBlockSize < 16:
                    self.error += "Invalid Block Size! Aborting!\n"
                sampleInfo = file.read(8)
                sampleInfoBytes = unpack('>Q', sampleInfo)[0]
                audioInfo.sampleRate = sampleInfoBytes >> 44
                audioInfo.channels = ((sampleInfoBytes >> 41) & 7) + 1
                audioInfo.bitsperSample = ((sampleInfoBytes >> 36) & 0x1F) + 1
                audioInfo.length = (sampleInfoBytes & 0x0000000FFFFFF) / float(audioInfo.sampleRate)

            else:
                self.error += "STREAMINFO BLOCK not first\n"
        if cmp(self.error, '') == 0
            return  audioInfo #Or None
        return None
    
