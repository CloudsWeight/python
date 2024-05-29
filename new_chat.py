import speech_recognition as sr 

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Speech!")
		audio = r.listen(source)
		return audio 

def sphinx_recognize(audio):
	r = sr.Recognizer()
	audio = audio 
	try:
		print(f"Sphinx thinks: {r.recognize_sphinx(audio)}")
	except sr.UnknownValueError:
		print("Sphinx errored..")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))

if __name__ == '__main__':
	audio = get_audio()

	sphinx_recognize(audio)