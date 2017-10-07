#!/usr/bin/env python

import argparse
import mne
import numpy as np
from scipy import io

if __name__ == '__main__':
    
    # parser = argparse.ArgumentParser(prog='fif2mat',
    #                                  description='converts raw EEG data in FIF format into MAT format;'
    #                                              'events are stored in an extra file in EEGLab format.')

    # parser.add_argument('fif_filepath',
    #                     help='path to the input FIF file')

    # parser.add_argument('eeg_filepath',
    #                     help='path to the output MAT file for the raw EEG data')

    # parser.add_argument('events_filepath',
    #                     help='path to the output MAT file for the events')


    # args = parser.parse_args()

    file_list = ['P01-raw', 'P04-raw', 'P05-raw', 'P06-raw', 'P07-raw', 'P09-raw', 'P11-raw', 'P12-raw', 'P13-raw', 'P14-raw' ]
  
    for file in file_list:

        fif_filepath = '../MIIR_dataset/fif_files/' + file + '.fif'
        eeg_filepath = '../MIIR_dataset/mat_files/eeg/' + file
        events_filepath = '../MIIR_dataset/mat_files/events/' + file

        print 'loading raw data from ', fif_filepath
        raw = mne.io.Raw(fif_filepath, preload=True, verbose=True)
        data, time = raw[:,:]

        print 'saving raw data to', eeg_filepath
        io.savemat(eeg_filepath, dict(data=data), oned_as='row')

        events = mne.find_events(raw, stim_channel='STI 014', shortest_event=0)

        # EEGLab event structure: type, latency, urevent
        # Event latencies are stored in units of data sample points relative to (0) 
        # the beginning of the continuous data matrix (EEG.data).
        eeglab_events = [[event[2], event[0], 0] for event in events]
        eeglab_events = np.asarray(eeglab_events, dtype=int)

        print 'saving events to', events_filepath
        io.savemat(events_filepath, dict(data=eeglab_events), oned_as='row')

    
