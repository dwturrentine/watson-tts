"""Authenticate"""

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


url = 'https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/8b9955d4-dccd-4d6b-a85a-75f91067d823'
apikey = ''

#setup Service
authenticator =IAMAuthenticator(apikey)
#New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
#Set Service on URL
tts.set_service_url(url)

"""Convert String"""
with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

#Convert from file

with open('script.txt', 'r') as f:
    text = f.readlines()
    print(text)
    # Relace new line indicator with blank space - cocatenate all together
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)
    print(text)

with open('./script.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
