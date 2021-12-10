import speech_recognition as sr
x=0
r = sr.Recognizer()
with sr.Microphone() as source:
    # print(source)
    print("start")
    # playsound("signal.mp3")
    audio = r.record(source, duration=5)  # บันทึกเสียง 5 วินาท
    # print(type(audio))# ี
    print("finish")
    # playsound("signal.mp3")
    # print(audio)
try:
    text = r.recognize_google(audio, language = 'en')
    print(text)
except:
    text = "Try again please"
if "room a" in text:
    x=1
    print(x)
