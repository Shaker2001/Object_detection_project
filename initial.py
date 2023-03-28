import wave
obj = wave.open('ahmed.wav', 'rb')
print("number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("framerate", obj.getframerate())
print("number of frames", obj.getnframes())
print("parameters:", obj.getparams())
frames = obj.readframes(-1)
obj_new = wave.open('ahmed_new.wav', 'wb')  # create a new file
obj_new.setnchannels(2)  # set number of channels
obj_new.setsampwidth(2)  # set sample width
obj_new.setframerate(48000)
obj_new.setnframes(495616)
obj_new.writeframes(frames)
obj_new.close()
