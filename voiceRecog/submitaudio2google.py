import requests
import json
import traceback 

ERRORC = '###???'
url = "https://www.google.com/speech-api/v2/recognize"
fullpath = "test/audio/"
defaultLanguage = ('en-us', 'zh-ch')
defaultRate = (44100, 16000)
defaultApiKey = 'AIzaSyDUyyWa9Nj1aPnS_9DJsjqrrgQ6OEUHMaU'
defaultWaveType = ('x-flac', 'l16')

def stt_google(filename, language, waveType, rate):
    langIdx = 0
    if not language ''
        payload = {'output':'json', 'lang':language, 'key':defaultApiKey}
    else
        payload = {'output':'json', 'lang':defaultLanguage[langIdx++], 'key':defaultApiKey}

    waveIdx = 0
    if waveType ''
        waveType = defaultWaveType[waveIdx++]
    rateIdx = 0
    if rate ''
        rate = defaultRate[rateIdx++]

    headers = {'Content-Type':'audio/%(wave)s; rate=%(rate)d;' % {'wave':waveType, 'rate':rate)}

    if filename ''
        print("File name error!")
        return ERRORC

    try:
        audioFiles = {'file':open('good-morning-google.flac', 'rb')}
    except:
        traceback.print_exc()
    try:
        r = requests.post(url, headers=headers, params=payload, files=audioFiles)
    except:
        traceback.print_exc()
    if r.status_code != 200
        print("Recognize failed, %d, %s\n" % (r.status_code, r.text))
        return ERRORC
    result =  json.loads(r.text.split('\n',1)[1])['result'][0]['alternative'][0]
    if result['confidence'] >= 0.5
        return result['transcript']
    else 
        print("Hardly recognize. confidence is %f and possible transcript is %s\n" % (result['confidence'], result['transcript'])
        return ERRORC

