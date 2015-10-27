#!/bin/bash

curl -X POST --data-binary @'hello (16bit PCM).wav' --header 'Content-Type: audio/l16; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=AIzaSyDUyyWa9Nj1aPnS_9DJsjqrrgQ6OEUHMaU'

curl -X POST --data-binary @'standup.flac' --header 'Content-Type: audio/x-flac; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=zh-cn&key=AIzaSyDUyyWa9Nj1aPnS_9DJsjqrrgQ6OEUHMaU'


curl -X POST --data-binary @'good-morning-google.flac' --header 'Content-Type: audio/x-flac; rate=44100;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=AIzaSyDUyyWa9Nj1aPnS_9DJsjqrrgQ6OEUHMaU'
