#! /usr/bin/env python2

import sys
import wave

import array

import matplotlib.pyplot as plt

# Global variables

samples = []
peakY = []
peakX = []


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

        plt.plot(samples)
        plt.ylabel('Amplitude')
        plt.show()


def findPeaks():
        LEFT_MIN_AMP = 2000
        WAVE_PEAK_TIME = 44100 * 10/1000 # 100ms

        global peakY
        global peakX

        index = 0

        while index < len(samples):
                if samples[index] > LEFT_MIN_AMP :
                        tempRange = samples[index: index + WAVE_PEAK_TIME]
                        peakY.append(max(tempRange))
                        peakX.append(index)
                        index = index + 44100 # Skip a sec after a hit
                index = index + 1

def main():

        w = wave.open('./assets/left.wav', 'r')

        nchannels, sampwidth, framerate, nframes, comptype, compname = w.getparams()

        # Read the whole WAV at once
        frames = w.readframes(nframes)
        w.close()

        # Convert to 16bit samples
        global samples
        samples = array.array("h", frames)

        getWaveInfo(w)
        findPeaks()
        plotWave(w)

if __name__ == "__main__" :
        main()
