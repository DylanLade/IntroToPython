import pyaudio
import os, wave, pickle, sys
from sys import byteorder
from array import array
from struct import pack
from sklearn.neural_network import MLPClassifier

from Emotion import extract_feature

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000

SILENCE = 30

# Returns true if data is below the threshold
def is_silent(snd_data):
    return max(snd_data) < THRESHOLD

# Average the output volume
def normalize(snd_data):
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

# Trim the blank spot at the start and end
def trim(snd_data):
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
            
            elif snd_started:
                r.append(i)
        
        return r

    # Trim the left
    snd_data = _trim(snd_data)

    # Trim the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

# Add silence to the start and end of data 
def add_silence(snd_data, seconds):
    r= array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r

# Record from the microphone and return as signed shorts
def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)
    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_data:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True
        
        if snd_started and num_silent > SILENCE:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

# Records from the mic and outputs the resulting data to path
def record_to_file(path):
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


if __name__ == "__main__":
    model = pickle.load(open("result/mlp_Classifier.model", "rb"))
    loop = True
    while loop:
        print("Please Talk")
        filename = "test.wav"
        record_to_file(filename)
        features = extract_feature(filename, mfcc=True, chroma=True, mel=True).reshape(1,-1)
        result = model.predict(features)[0]
        print("result: " + result)

        choice = input("Would you like to record another?(y/n) ")
        if choice == 'y':
            loop = True
        else:
            sys.exit()