import googletrans
import speech_recognition
import gtts
import playsound
#voice translation agent can also be made using  pyttsx3 library 
recognizer = speech_recognition.Recognizer()

try:
    with speech_recognition.Microphone() as source:
        print("Speak Now")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language="en")
        print("Speech Recognition:", text)

        translator = googletrans.Translator()
        translation = translator.translate(text, dest="ur")
        print("Translation:", translation.text)

        converted_audio = gtts.gTTS(translation.text, lang="ur")
        converted_audio.save("urdu.mp3")
        playsound.playsound("urdu.mp3")

except speech_recognition.UnknownValueError:
    print("Speech Recognition could not understand audio")

except speech_recognition.RequestError as e:
    print(f"Speech Recognition request failed; {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")