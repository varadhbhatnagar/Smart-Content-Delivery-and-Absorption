import speech_recognition as sr 
import argparse

def main():
	if args.mode == 'file':
		AUDIO_FILE = args.audio_file 
		TEXT_FILE = args.text_file
		r = sr.Recognizer() 
	  
		with sr.AudioFile(AUDIO_FILE) as source: 
		    audio = r.record(source)   
		  
		try: 
		    print("The audio file contains: " + r.recognize_google(audio)) 
		  
		except sr.UnknownValueError: 
		    print("Google Speech Recognition could not understand audio") 
		  
		except sr.RequestError as e: 
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	
	else if args.mode == 'live':
		pass
	else
		print("Invalid Mode")	
		


if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument('--mode', default='file', choices=['file','live'], help='Speech Source')
	parser.add_argument('--audio_file', help='Audio File in WAV format containing Speech')
	parser.add_argument('--text_file', help='Text File contaning the corresponding Topic')
	args = parser.parse_args()

	main() 




