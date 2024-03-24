import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.startLoop(False)
    machine.iterate()
machine.runAndWait()

def input_instruction():
    global instruction
    instruction = " "
    try:
        with aa.Microphone() as origin:
            print("listening....")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Jack" in instruction:
                instruction = instruction.replace('Jack','')
                # print(instruction)
            return instruction
            


    except:
        pass
    
    return instruction

def play_Jack():

    instruction = input_instruction()   
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play" , "")
        talk("playing" + song)
        print("Play this song on YouTube")
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")  
        talk("Current Time " + time)
        print("Current Time " + time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d/%m/%y")  
        talk("Today's date" + date)
        print("Today's date : " ,date)
    elif "how are you" in instruction:
        talk("I am fine,how about you")
        print("I am fine,how about you")
    elif "what is your name" in instruction:
        talk("I am Jack,what can I do for you?")
        print("I am Jack,what can I do for you?")
    elif "who is" in instruction:
        human = instruction.replace("who is","")
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)
    else:
        talk("Please repeat")

play_Jack()


