#deep learning
#convoluted neural networks, paper on nature


import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import numpy as np

def pad_audio_front_n_back(data, fs, time_ms ):
    shape = data.shape
    #ms = time_ms/1000
    # calculae target number of samples for milliseconds
    num_target_samples = int(fs * time_ms )
    #print time_ms
    print num_target_samples
    # create shape
    number_to_pad = num_target_samples - shape[0]
    print number_to_pad
    print ("padding with %s milliseconds of silence" % str(number_to_pad / fs))
    shape = (number_to_pad,) + shape[1:]

    #print "shape"
    #print shape
    #print "shape[0]"
    #print shape[0]
    pad_data_front = np.ones(shape)
    pda_data_back = np.ones(shape)
    #pad_data.fill(0.13089716)
    #print pad_data
    #print "pad.shape"
    #pad_shape = pad_data.shape
    #print pad_shape
    #print "pad_data shape[0]"
    #print pad_shape[0]
    #pad_data.fill(0.13089716)

    # check if there is an audio file to append data to
    #pad the front if is 1
    print len(shape)
    if shape[0] > 1:

        if len(shape) > 1:
            data= np.vstack((data,  pda_data_back))
            print "in side vstack"
            #data = np.vstack((pad_data_front,data ))
        else:
            print "in side hstack"
            np.hstack((data, pda_data_back))
            #np.hstack((pad_data_front, data))
    return data


def pad_audio(data, fs, time_ms,pad_front=0):
    # calculate the number of zeroes for the shape
    shape = data.shape
    #ms = time_ms/1000
    # calculae target number of samples for milliseconds
    num_target_samples = int(fs * time_ms )
    print num_target_samples
    # create shape
    number_to_pad = num_target_samples - shape[0]
    print number_to_pad
    print ("padding with %s milliseconds of silence" % str(number_to_pad / fs))
    shape = (number_to_pad,) + shape[1:]
    #print "shape"
    #print shape
    #print "shape[0]"
    #print shape[0]
    pad_data = np.ones(shape)
    #pad_data = np.random.rand(shape)
    #pad_data.fill(4.5555555)
    print pad_data
    #print "pad.shape"
    #pad_shape = pad_data.shape
    #print pad_shape
    #print "pad_data shape[0]"
    #print pad_shape[0]
    #pad_data.fill(0.13089716)

    # check if there is an audio file to append data to
    #pad the front if is 1
    if pad_front == 0:
        if shape[0] > 1:
            if len(shape) > 1:
                data= np.vstack((data,  pad_data))
            else:
                data = np.hstack((data, pad_data))
    else:
        if shape[0] > 1:
            if len(shape) > 1:
                data = np.vstack((pad_data, data))
            else:
                data= np.hstack((pad_data, data))

    return data

FRONT = 1
BACK = 0
file_wav = 'T0000125.WAV' # """static name of the wav file"""
"""read the wav file """
rate, data = wavfile.read(file_wav)
print np.shape(data)
#data = pad_audio_front_n_back(data,rate,2)

data = pad_audio(data,rate,2,FRONT)

data = pad_audio(data,rate,3,BACK)
#print np.shape(data)
#print rate #rate 250 for all the files???
#print np.shape(rate)
"""window segments"""
nfft = 256  # Length of the windowing segments
"""sampling frequency"""
fs = 256
"""create spectrogram"""
pxx, freqs, bins, im = plt.specgram(data, nfft, fs)

#print "\npxx"
#print np.shape(pxx)
#print pxx
#print "\nfreq"
#print np.shape(freqs)
#print freqs # array of 128 values?
#print "\nbins"
#print np.shape(bins)
#print bins
#print "\nim"
#print im
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
plt.axis('on')
plt.ylabel("Frequency [kHz]")
plt.xlabel("Time [ms]")
plt.show()
#plt.savefig('T0000223-3.png', dpi=100,frameon='false', aspect='normal', bbox_inches='tight', pad_inches=0)  # Spectrogram saved as a .png

