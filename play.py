import math
from pyaudio import PyAudio

BITRATE = 8000     #number of frames per second

FREQUENCIES = {
    "C4":   261.63, #C4 in Hz
    "C#4":  277.18, #C sharp
    "D4":	293.66,
    "D#4": 	311.13,
    "E4":	329.63,
    "F4":	349.23,
    "F#4":	369.99,
    "G4":	392.00,
    "G#4":	415.30,
    "A4":	440.00,
    "A#4": 	466.16,
    "B4":	493.88,
    "C5":	523.25,
    "C#5": 	554.37,
    "D5":	587.33,
    "D#5": 	622.25,
    "E5":	659.25,
    "F5":	698.46,
    "F#5": 	739.99,
    "G5":	783.99,
    "G#5": 	830.61,
    "A5": 	880.00,
    "A#5":  932.33,
    "B5":   987.77,
    "B#5": 	932.33,
    "C6": 	1046.50,
    "D6":	1108.73,
    "D#6": 	1174.66,
    "E6":	1318.51
}

LENGTH = 0.5        #seconds to play sound for each note

MUSIC = ["F#5", "E5", "D5", "C#5", "B4", "A4", "B4", "C#5"] # cannon in D major

NUMBEROFNOTES = len(MUSIC)

NUMBEROFFRAMES = int(BITRATE * LENGTH)  #frames per note
WAVEDATA = ''

for y in range(NUMBEROFNOTES):
    FREQUENCY = FREQUENCIES[MUSIC[y]]
    print(MUSIC[y])
    #generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))
    print(WAVEDATA)
p = PyAudio()
stream = p.open(format = p.get_format_from_width(1, unsigned=True), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
