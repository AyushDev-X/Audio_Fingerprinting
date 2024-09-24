import sounddevice as sd
import soundfile as sf

# Set parameters for audio recording
duration = 5  
# You can adjust the duration of recording
sample_rate = 44100
channels = 1

print("Recording...")

# Record audio from the microphone
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
sd.wait()  # Wait until recording is finished

print("Recording finished.")

# Save the recorded audio to a file
file_name = "recorded_audio.wav"
sf.write(file_name, audio_data, sample_rate)

print(f"Audio saved as {file_name}")

