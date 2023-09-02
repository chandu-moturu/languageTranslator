import streamlit as st
import googletrans
import speech_recognition
import gtts
from pydub import AudioSegment
from pydub.playback import play

st.title("Optimized Language Translator")

input_lang = st.selectbox("Select the input language", googletrans.LANGUAGES.values())
output_lang = st.selectbox("Select the output language", googletrans.LANGUAGES.values())

if st.button("Start Voice Input"):
    st.write("Listening...")

    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.write("Speak now:")
        voice = recognizer.listen(source, timeout=10)
        st.write("Processing...")

    try:
        text = recognizer.recognize_google(voice, language=input_lang, show_all=True)['alternative'][0]['transcript']
        st.write(f"Original Text ({input_lang}):")
        st.write(text)

        translator = googletrans.Translator(service_urls=["translate.google.com", "translate.deepl.com"])
        translation = translator.translate(text, dest=output_lang)
        st.write(f"Translated Text ({output_lang}):")
        st.write(translation.text)


    except:
        st.error('I am unable to understand. Please try again')



