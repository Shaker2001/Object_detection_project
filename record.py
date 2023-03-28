import wave
import pyaudio

frames_per_buffer = 3200
_format = pyaudio.paInt32
channels = 1
sample_rate = 16000

p1 = pyaudio.PyAudio()  # first create an interface to PortAudio
p = p1.open(  # second open a new Stream object to write the WAV file to
    format=_format,
    channels=channels,
    rate=sample_rate,
    input=True,
    frames_per_buffer=frames_per_buffer

)
print("Watch out !!!!!!!!!--->> Recording...")

# Record for 10 seconds
# we now will save the frames in a list and
seconds = 5
frames = []
for i in range(0, int(sample_rate / frames_per_buffer * seconds)):
    data = p.read(frames_per_buffer)  # read a chunk of frames at one operation
    frames.append(data)
p.stop_stream()
p.close()
p1.terminate()

# so now we have the frames in a list and we can write them to a file
test = wave.open('tost.wav', 'wb')  # create a new file
test.setnchannels(channels)  # set number of channels
test.setsampwidth(p1.get_sample_size(_format))  # set sample width
test.setframerate(sample_rate)  # set sample rate
# write frames in binary format and combine all elements in our list into binary stream
test.writeframes(b''.join(frames))
test.close()
