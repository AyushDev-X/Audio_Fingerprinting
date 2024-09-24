import wave
wave_obj = wave.open('/content/recorded_audio.wav','rb')

# sampling frequency
sample_freq = wave_obj.getframerate()
print('Sampling Frequency: ',sample_freq)

#total samples
n_samples = wave_obj.getnframes()
print('Total number of samples are: ',n_samples)

#total duration
length = n_samples/sample_freq
print('Total duration: ',length)

#no. of channels
n_channels=wave_obj.getnchannels()
print('Number of channels: ',n_channels)

signal_wave = wave_obj.readframes(n_samples)
print('Type of signal wave: ',type(signal_wave))

# converting data into 16-bits signed integer array
import numpy as np
signal_array = np.frombuffer(signal_wave,dtype=np.int16)
print('Samples in signal array: ',len(signal_array))

#channel separation
left_channel = signal_array[0::2]
right_channel = signal_array[1::2]
print('Length of left channel: ',len(left_channel))

# timestamps
times = np.linspace(0,n_samples/sample_freq,num=n_samples)


# plotting the Amplitude  v/s Time

# left channel
import matplotlib.pyplot as plt
plt.figure(figsize=(10,3))
plt.plot(times[:len(left_channel)], left_channel)
plt.title('Left Channel')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')

plt.show()

# plotting the Amplitude v/s Frequency response
import matplotlib.pyplot as plt
plt.figure(figsize=(10,3))
plt.specgram(left_channel,Fs=sample_freq, vmin=-30, vmax=30)
plt.title('Left Channel')
plt.xlabel('Time(s)')
plt.ylabel('Frequency(Hz)')
plt.colorbar()
plt.show()

print()
# Extracting unique signature
import librosa
import hashlib

def generate_audio_signature(audio_file):

    # coverting integer type array to floating point
    signal_array_fp = signal_array.astype(np.float32)
    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=signal_array_fp, sr=sample_freq)
   # plt.plot(mfccs)

    # Flatten the MFCCs into a 1D array
    flattened_mfccs = mfccs.ravel()
    plt.plot(flattened_mfccs)

    # Convert the array to bytes
    signature_bytes = flattened_mfccs.tobytes()

    # Hash the signature bytes using SHA-256
    hashed_signature = hashlib.sha1(signature_bytes).hexdigest()

    return hashed_signature

# Example usage
audio_file = '/content/recorded_audio.wav'
signature = generate_audio_signature(audio_file)
print("Audio Signature:", signature)