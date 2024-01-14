from gtts import gTTS


def get_audio(text):
    tts = gTTS(text=text, lang= 'en', slow=False)
    output= "/sound/output.wav"
    #tts.save(output)
    with open('ouput.wav', 'wb') as f:
        tts.write_to_fp(f)

if __name__ == "__name__":
    get_audio("This is just my opinion!")
