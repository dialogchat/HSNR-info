#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gtts import gTTS
from tempfile import TemporaryFile
from pygame import mixer
import os, time
import os.path
import sys
import json


try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

#insert your client token by api.ai:
CLIENT_ACCESS_TOKEN = '27af35bde3364e6ea5c2efcd2eef097c'

#CLIENT_ACCESS_TOKEN:
#client hsnr-info: 27af35bde3364e6ea5c2efcd2eef097c
#Developer access token:

def hibye(utterance):
	#-------------------------------------------------------------------
	#create welcome/good bye dialogues
	#tts: gtts (mp3)
	#-------------------------------------------------------------------
    print ("Honina: "+ utterance)
    tts = gTTS(text = utterance, lang='de')        #server tts query
    tts.save(utterance[0:2]+".mp3")                #save file to disk
    #os.startfile(utterance[0]+".mp3")             #win play file from disk
    os.system("mpg321 -q "+utterance[0:2]+".mp3")  #linux play file from disk
    os.remove(utterance[0:2]+".mp3")
	

def qaquery(user_input, ai):
	#-------------------------------------------------------------------
	#create qa query pairs
	#nlp: api.ai (json)
	#tts: gtts (mp3)
	#-------------------------------------------------------------------
    request = ai.text_request() #http request 
    request.query = user_input  #json query
    response = json.loads(request.getresponse().read().decode('utf8')) #json to dict
    utterance = response['result']['fulfillment']['speech'] #answer
    print ("Honina: "+utterance) 				  #print answer
    tts = gTTS(text = utterance, lang='de')       #server tts query
    tts.save(utterance[0:2]+".mp3")               #save file to disk
    #os.startfile(utterance[0]+".mp3")            #win play file from disk
    os.system("mpg321 -q "+utterance[0:2]+".mp3") #linux play file from disk
    os.remove(utterance[0:2]+".mp3")
    
      
def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    user_input=''  #init user_input
    
    #welcome dialogues:
    hibye("Willkommen an der HSNR!!")
    hibye("Mein Name ist Honina.")
    hibye("Was moechtest du wissen?")
    
    #main dialogue:
    while user_input != 'quit':
        user_input = raw_input("You: ") #get user input (string)
        #user_input = input("You: ") #get user input (string)
        if user_input != 'quit':
			qaquery(user_input, ai)
			
	#good bye dialogue:
	if user_input == 'quit':
		hibye("Ok tschuess.")	

	
if __name__ == '__main__':
    main()
