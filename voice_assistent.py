import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import pywhatkit as kit
from sys import exit
from os import listdir

def sptext():
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		recognizer.adjust_for_ambient_noise(source)
		recognizer.pause_threshold = 1
		audio = recognizer.listen(source)
		try:
			print('recognizing...')
			data = recognizer.recognize_google(audio, language = 'en-in')
			print(data) 
			return data
		except sr.UnknownValueError:
			return 'Sorry, could not understand'



def txtspeech(user_voice):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices)
	rate = engine.getProperty('rate')
	engine.setProperty('rate',150)
	engine.say(user_voice)
	engine.runAndWait()
	
	
"""	
#txtspeech("I am a student and I am pursuing Masters in Computer Science.")	
	
txtspeech(sptext())	


#sptext()
"""




if __name__ == '__main__':

		data1 = sptext().lower()

		if 'hello laptop' in data1 or 'hey laptop' in data1 or 'hey-hey laptop' in data1 or 'he laptop' in data1 or 'hai laptop' in data1 or 'hee laptop' in data1 or 'hay laptop' in data1 or 'oo laptop' in data1 or 'oye laptop' in data1 or 'o laptop' in data1:
			take_order = "Hello sir! How can I help you?"
			txtspeech(take_order)
			
		
			while True:
			
				data1 = sptext().lower()
						
				if 'your name' in data1:
					name = "My name is Laptop"
					txtspeech(name)
					
				elif 'your age' in data1:
					age = "I am 1 year old"
					txtspeech(age)	
					
				elif 'old are you' in data1:
					age = "I am 1 year old"
					txtspeech(age)	
						
				elif 'time' in data1:
					time = datetime.datetime.now().strftime('%I:%M %p')
					print(time)
					txtspeech(time)			
					
				elif 'youtube' in data1:
					webbrowser.open('https://www.youtube.com/')	
					
				elif 'my channel' in data1:
					webbrowser.open('youtube.com/c/AnimeStar022?sub_confirmation=1')	
						
				elif 'pinterest' in data1:
					webbrowser.open('https://in.pinterest.com/')	
						
				elif 'pinterest profile' in data1:
					webbrowser.open('https://in.pinterest.com/vishnulohkna/')
					
				elif 'krishna bhajan' in data1 or 'krishn bhajan' in data1:
					webbrowser.open('https://www.youtube.com/watch?v=jl4Y7fzmhfE&list=PLUtuusAiDCARisDvSvCetWNCoMCE9nwlD')			
					
				elif 'instagram profile' in data1:
					webbrowser.open('https://www.instagram.com/itachiuzumaki022/')
				
				elif 'insta profile' in data1:
					webbrowser.open('https://www.instagram.com/itachiuzumaki022/')		
				
				elif 'instagram account' in data1:
					webbrowser.open('https://www.instagram.com/itachiuzumaki022/')
				
				elif 'insta account' in data1:
					webbrowser.open('https://www.instagram.com/itachiuzumaki022/')	
				
				elif 'instagram' in data1:
					webbrowser.open('https://www.instagram.com/')
				
				elif 'open insta' in data1:
					webbrowser.open('https://www.instagram.com/')	
					
				elif 'jokes' in data1:
					jokes = pyjokes.get_jokes(language = 'en', category = 'neutral')
					for i in range(len(jokes)):
						if i >= 5:
							break
						txtspeech(jokes[i])
				elif 'joke' in data1:
					joke = pyjokes.get_joke(language = 'en', category = 'neutral')
					print(joke)
					txtspeech(joke)
						
				elif 'song' in data1:
					songs = listdir('/home/dhruv051/Desktop/songs')
					print(songs)
						
					webbrowser.open("/home/dhruv051/Desktop/songs"+'/'+ songs[-1])
				
				elif 'music' in data1:
					print('What is the music or song name?')
					txtspeech('What is the music or song name?')	
					musicName = sptext()
					kit.playonyt(musicName)	
				
					
				elif 'laptop close' in data1 or 'bye bye laptop' in data1 or 'laptop exit' in data1 or 'buy laptop' in data1 or 'bye laptop' in data1:
					greeting = "Thank-you sir, "
					time = datetime.datetime.now().strftime('%I:%M %p')
					if int(time[:2]) >= 5 and int(time[:2]) < 12:
						if time[-2:] == 'PM':
							greet = 'good evening'
							print(greeting+greet)
							txtspeech(greeting+greet)
							exit()
					
					elif int(time[:2]) >= 3 and int(time[:2]) < 12:
						if time[-2:] == 'AM':
							greet = 'good morning'
							print(greeting+greet)
							txtspeech(greeting+greet)
							exit()		
					
					elif int(time[:2]) >= 12 and int(time[:2]) < 5:
						if time[-2:] == 'PM':
							greet = 'good afternoon'
							print(greeting+greet)
							txtspeech(greeting+greet)
							exit()	
					
					else:
						greet = 'Thank-you sir'
						print(greet)
						txtspeech(greet)
						exit()				
						
				else:
					txtspeech('Could not recognize!')
					print('Could not recognize!')
			    
			
		else:
			txtspeech('Could not recognize!')		



