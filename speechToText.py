import os
import pyaudio
from vosk import Model, KaldiRecognizer

# Load model
model = Model("C:/Users/u/vosk-model-small-ko-0.22/vosk-model-small-ko-0.22")

# Create recognizer
rec = KaldiRecognizer(model, 16000)

# Initialize pyaudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Recognize speech
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())