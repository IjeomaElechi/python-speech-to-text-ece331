import speech_recognition as sr

r = sr.Recognizer()
print("Recognising my speech...")

tag = sr.AudioFile('elechi.wav')
with tag as source:
    audio = r.record(source)
    
    type(audio)
    
    r.recognize_google(audio)
    
    print("Ending my speech Recognition..")
    
    
   #ECE 331 Project for a python speech to text program 
    
    