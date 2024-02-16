from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang= "ko")
    tts.save("voice.mp3")
    
speak("안녕하세요. 저는 전병현이라고합니다. 최종 금액은 38000원입니다.")