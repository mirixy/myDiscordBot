import pyttsx3

def voicePlay(string):

    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    #engine.say(f"{string}")
    #try:
    #    engine.runAndWait()
    #except Exception as e:
    #    pass
    #engine.runAndWait()
    engine.save_to_file(text="Hello darkness my old friend", filename="output.wav")
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    voicePlay("Hello Darling")
