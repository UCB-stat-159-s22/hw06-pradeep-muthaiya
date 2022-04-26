
import pytest
from scipy.interpolate import interp1d
import matplotlib.mlab as mlab
#import sys
import os
import numpy as np
#sys.path.append(os.path.join(os.path.dirname('test_utils.py'), '..'))

from ligotools import utils


def test_whiten():
    Pxx_H1, freqs = mlab.psd(np.arange(10000), Fs = 4096, NFFT = 16384)
    psd_H1 = interp1d(freqs, Pxx_H1)
    test = utils.whiten(np.arange(10000),psd_H1,.00235242)[0]
    assert test == -22.328077707094554
    
def test_write_wavfile():
    utils.write_wavfile("hello.wav",523, np.arange(1000))
    assert os.path.exists('hello.wav')
    os.remove('hello.wav')
    
    
def test_reqshift():
    test = utils.reqshift(np.arange(100),fshift=400,sample_rate=.0131)[0]
    assert test == 0.0
    
def test_make_plot():
    assert utils.make_plot(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, False) == 0       
       


