#! /usr/bin/env python2

import sys
import wave

import array

import matplotlib.pyplot as plt

def getWaveInfo(w):
        """

        Arguments:
        - `w`: Wave_read instance
        """
        print "Num of channels    : ", w.getnchannels()
        print "Sample Width       : ", w.getsampwidth()
        print "Sampling Frequency : ", w.getframerate()
        print "Number of frames   : ", w.getnframes()
        print "Compression type   : ", w.getcomptype()
        print "compression name   : ", w.getcompname()

def plotWave(w):

        nchannels, sampwidth, framerate, nframes, comptype, compname = w.getparams()

        # Read the whole WAV at once
        frames = w.readframes(nframes)
        w.close()

        # Convert to 16bit samples
        samples = array.array("h", frames)

        plt.plot(samples)
        plt.ylabel('Amplitude')
        plt.show()


def main():

        w = wave.open('./assets/left.wav', 'r')

        getWaveInfo(w)
        plotWave(w)

if __name__ == "__main__" :
        main()
