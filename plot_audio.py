import matplotlib.pyplot as plt
import numpy as np
import wave

# Read the wave file
obj = wave.open('ahmed.wav', 'rb')
sample_rate = obj.getframerate()
num_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()
# Convert the wave file to an array
time_audio = num_samples/sample_rate    # time in seconds
print("time_audio: ", time_audio)
signal = np.frombuffer(signal_wave, dtype=np.int32)
times = np.linspace(0, time_audio, num=num_samples)
plt.figure(figsize=(15, 5))
plt.plot(times, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.xlim(0, time_audio)
plt.show()  # Display the plot
