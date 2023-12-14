import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import pyttsx3

# Function to analyze emotions in the audio file
def analyze_emotions(audio_path):
    # Use a simple emotion analysis model or API here
    # For simplicity, let's assume it returns a dictionary with emotion percentages
    emotion_results = {
        "anger": 10,
        "disgust": 5,
        "fear": 15,
        "happiness": 40,
        "pleasant_surprise": 10,
        "sadness": 10,
        "neutral": 10,
    }
    return emotion_results

# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Streamlit app
def main():
    st.title("Audio Emotion Analyzer")

    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav", start_time=0)

        if st.button("Analyze Emotions"):
            st.info("Analyzing emotions... Please wait.")
            try:
                # Convert audio file to wav format
                audio = AudioSegment.from_file(uploaded_file)
                audio.export("audio.wav", format="wav")

                # Perform emotion analysis
                emotion_results = analyze_emotions("audio.wav")

                # Display emotion percentages
                st.subheader("Emotion Percentages:")
                for emotion, percentage in emotion_results.items():
                    st.write(f"{emotion.capitalize()}: {percentage}%")

                # Choose the dominant emotion
                dominant_emotion = max(emotion_results, key=emotion_results.get)
                st.success(f"Dominant Emotion: {dominant_emotion.capitalize()}")

                # Text-to-speech output
                text_to_speech(f"The dominant emotion is {dominant_emotion}.")
            except Exception as e:
                st.error(f"Error analyzing emotions: {str(e)}")

if __name__ == "__main__":
    main()

