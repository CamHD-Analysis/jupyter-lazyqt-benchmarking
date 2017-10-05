#!/usr/bin/env python

from pycamhd import native as pycamhd
import numpy as np
import random


# This file is in the overlay on Berna
filename_overlay = '/data/CAMHDA301-20160724T030000Z.mov'

# This file is _not_ in the overlay on Berna
filename_nonoverlay = 'https://rawdata.oceanobservatories.org/files/RS03ASHS/PN03B/06-CAMHDA301/2016/11/13/CAMHDA301-20161113T000000Z.mov'


def check_image(img):

    assert isinstance(img, np.ndarray)

    shape = img.shape
    assert shape[2] == 3   # RGBA?
    assert shape[1] == 1920
    assert shape[0] == 1080


def do_get_image(benchmark, filename):
    moov_atom = pycamhd.get_moov_atom(filename)
    frame_count = pycamhd.get_frame_count(filename, moov_atom)
    img=benchmark(pycamhd.get_frame, filename, int(random.uniform(0,frame_count)), moov_atom=moov_atom)
    check_image(img)

def test_native_np_overlay(benchmark):
    do_get_image(benchmark, filename_overlay)

def test_native_np_nonoverlay(benchmark):
    do_get_image(benchmark, filename_nonoverlay)
