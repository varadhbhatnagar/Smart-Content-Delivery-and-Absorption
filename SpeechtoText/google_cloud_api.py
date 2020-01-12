import io
import os
import argparse

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 

def main():
	client = speech.SpeechClient()

	# The name of the audio file to transcribe
	audio_file = args.audio_file
	text_file = args.text_file

	with open(text_file, 'r') as file:
    		text = file.read().replace('\n', '')

	# Loads the audio into memory
	with io.open(audio_file, 'rb') as audio_file:
	    content = audio_file.read()
	    audio = types.RecognitionAudio(content=content)

	config = types.RecognitionConfig(
	    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16, audio_channel_count = 2, language_code='hi-IN')

	# Detects speech in the audio file
	response = client.recognize(config, audio)

	for result in response.results:
	    print('Transcript: {}'.format(result.alternatives[0].transcript))
	
	transcript = result.alternatives[0].transcript
	print(fuzz.token_set_ratio(transcript, text))


if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument('--mode', default='file', choices=['file','live'], help='Speech Source')
	parser.add_argument('--audio_file', help='Audio File in WAV format containing Speech')
	parser.add_argument('--text_file', help='Text File contaning the corresponding Topic')
	args = parser.parse_args()

	main() 

