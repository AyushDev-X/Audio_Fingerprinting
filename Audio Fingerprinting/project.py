import wave
wave_obj = wave.open('/content/file_example_WAV_1MG.wav','rb')

# sampling frequency
sample_freq = wave_obj.getframerate()
print(sample_freq)

#total samples
n_samples = wave_obj.getnframes()
print(n_samples)

#total duration
length = n_samples/sample_freq
print(length)

#no. of channels
n_channels=wave_obj.getnchannels()
print(n_channels)

signal_wave = wave_obj.readframes(n_samples)
print(type(signal_wave))

# converting data into 16-bits signed integer array
import numpy as np
signal_array = np.frombuffer(signal_wave,dtype=np.int16)
print(len(signal_array))

#channel separation
left_channel = signal_array[0::2]
right_channel = signal_array[1::2]
print(len(left_channel),len(right_channel))

# timestamps
times = np.linspace(0,n_samples/sample_freq,num=n_samples)

# plotting the Amplitude  v/s Time 

# left channel
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(times,left_channel)
plt.title('Left Channel')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show()

# right channel
plt.figure(figsize=(10,5))
plt.plot(times,right_channel)
plt.title('Right Channel')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.show()

# plotting the Amplitude v/s Frequency response
