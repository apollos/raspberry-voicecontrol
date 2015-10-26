#!/bin/bash

curl -X POST --data-binary @'hello (16bit PCM).wav' --header 'Content-Type: audio/l16; rate=16000;' 'https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=AIzaSyDUyyWa9Nj1aPnS_9DJsjqrrgQ6OEUHMaU'
