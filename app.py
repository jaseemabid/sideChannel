#! /usr/bin/env python3

import wave
w = wave.open('./assets/left.wav', 'r')

def getWaveInfo(w):
        """

        Arguments:
        - `w`: Wave_read instance
        """
        print ("Num of channels    : ", w.getnchannels())
        print ("Sample Width       : ", w.getsampwidth())
        print ("Sampling Frequency : ", w.getframerate())
        print ("Number of frames   : ", w.getnframes())
        print ("Compression type   : ", w.getcomptype())
        print ("compression name   : ", w.getcompname())

def main():
        getWaveInfo(w)


if __name__ == "__main__":
        main()
