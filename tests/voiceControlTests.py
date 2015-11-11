import logging
import logging.config
import os
import sys
from nose.tools import *

sys.path.append("..")
from voiceRecog import *


logging.config.fileConfig("logging.conf")

# create logger
logger = logging.getLogger("voiceCongrolTests")

def testRecgAudioType():
    filelist = os.listdir("audio")
    logger.info("Check the followed file(s):\n" + "\n".join(filelist))
    for filename in filelist:
        flacFile = flacType()
        flacFileInfo = flacFile.getAttribute("audoi/"+filename)
        if flacFileInfo is None:
            logger.info("audoi/"+filename + " is not a flac file")
            continue
        else:
            logger.info("audoi/"+filename + " Attributes as followed: audioFormat - %s, sampleRate - %5d, audioLanguage - %s, audio length - %d" % (flacFileInfo.audioFormat, flacFileInfo.sampleRate, flacFileInfo.audioLanguage, flacFileInfo.length))

            
        
