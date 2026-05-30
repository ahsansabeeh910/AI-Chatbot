from gtts import gTTS

def text_to_audio(text):

    speech = gTTS(text)

    speech.save("response.mp3")

    return "response.mp3"