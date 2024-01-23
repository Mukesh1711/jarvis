import speech_recognition as sr

listener = sr.Recoganiser()
try:
    with sr.Microphone() as source:
        print("Listening....")
        voice = listener.listen(source)
        command = listener.listen(source)
        print(command)
except:
    pass        