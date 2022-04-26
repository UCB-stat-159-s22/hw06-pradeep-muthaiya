# test_readligo.py

import pytest
import numpy as np
#import sys
#import os
#sys.path.append(os.path.join(os.path.dirname('test_readligo.py'), '..'))

from ligotools import readligo as rl

def test_dq_channel_to_seglist():
    x = {u'BURST_CAT1': np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
         'DEFAULT': np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1])}
    y = rl.dq_channel_to_seglist(x)
    assert y == [slice(0, 131072, None)]

def test_dq2segs():
    x = {'DEFAULT': np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1])}
    y = rl.dq2segs(x, 1)[0]
    assert y == (1, 33)
    
def test_FileList():
    y = rl.FileList()
    assert y.directory == '.'
    
def test_loaddata():
    y = rl.loaddata('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')
    assert y[0][0] == 2.177040281449375e-19