import io
import os
import argparse

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 


def stt(audio_file, text_file):
	client = speech.SpeechClient()

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
	res=""
	for result in response.results:
		print('Transcript: {}'.format(result.alternatives[0].transcript))
		res = res+(format(result.alternatives[0].transcript))

	return fuzz.token_set_ratio(res, text)
