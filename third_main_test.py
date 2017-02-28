#deep learning
#convoluted neural networks, paper on nature


import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal


file_wav = 'T0000223.WAV' # """static name of the wav file"""
"""read the wav file """
rate, data = wavfile.read(file_wav)
"""window segments"""
nfft = 256  # Length of the windowing segments
"""sampling frequency"""
fs = 256
"""create spectrogram"""
pxx, freqs, bins, im = plt.specgram(data, nfft, fs)

"""Create Second spectrogram """
"""
f: ndarray
    Array of sample frequencies.
t : ndarray
    Array of segment times.
Sxx : ndarray
    Spectrogram of x. By default, the last axis of Sxx corresponds to the segment times.
"""
#f, t, Sxx =signal.spectrogram(data,fs, window=('tukey', 0.25))
#plt.pcolormesh(t,f,Sxx)

#print data[100]

"""plot it"""
#plt.axis('on')
plt.ylabel("Frequency [kHz]")
plt.xlabel("Time [ms]")
plt.show()
#plt.savefig('T0000223.png', dpi=100,  # Dots per inch frameon='false', aspect='normal', bbox_inches='tight', pad_inches=0)  # Spectrogram saved as a .png