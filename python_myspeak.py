import os 
import pyttsx3
import datetime

today = datetime.date.today()

pyttsx3.speak("hellow sir hope you are fine, please provide us your name")
a = input("your name") 
print()
print("hello" +a)
pyttsx3.speak("hello" +a)
pyttsx3.speak("today date is")
print("today date is")
print(today)


pyttsx3.speak("hi, this is your persnol assitant , my name is harry, i can help you to saving your time,for opening some function as per your instructions, we can, open chrome browser, vlc player, calcultor,your pc settings, notepad, shut dwon your pc")
pyttsx3.speak("let me now how can i help for you")

while True:
 x=input("tell me what is your requirments:")
 x=x.lower()

 if((("run" in x)or("execute" in x)or("open" in x))and(("chrome"in x)or("browser" in x)or("search engine" in x)or("gooogle" in x))):
     pyttsx3.speak("please wait a moment while we opening chrome")
     os.system("chrome")

 elif((("run" in x)or("execute" in x)or("open" in x))and(("player" in x)or("vlc" in x)or("video player" in x))):
     pyttsx3.speak("please wait a moment while we opening video player")
     os.system("vlc")

 elif((("run" in x)or("execute" in x)or("open" in x))and(("calculator" in x)or("calc" in x)or("solution" in x))):
     pyttsx3>speak("please wait a moment while we opening caclculator")
     os.system("calc")

 elif((("run" in x)or("execute" in x)or("open" in x))and(("setting" in x)or("your pc settings" in x))):
     pyttsx3.speak("please wait a moment while we opening seting")
     os.system("start ms-settings:")

 elif((("run" in x)or("execute" in x)or("open" in x))and(("notepad" in x)or("editor" in x)or("text" in x))):
     pyttsx3.speak("please wait a moment while we opening notepad")
     os.system("notepad")

 elif("exit" in x)or("close" in x)or("quit"in x):
     break


 else:
     pyttsx3.speak("the instruction you give is incorrect, try again later")
     print("please try again")
