import numpy as np
import scipy.io

if __name__ == '__main__':
	# after saving the data in .mat files extract in python files
    mat_raw_eeg = scipy.io.loadmat('/home/tinkerers/pranav_sankhe/Perceived-Music-Information-Retrieval/MIIR_dataset/mat_files/eeg/P01-raw.mat')          # 69 x 2478166
    mat_events_eeg = scipy.io.loadmat('/home/tinkerers/pranav_sankhe/Perceived-Music-Information-Retrieval/MIIR_dataset/mat_files/events/P01-raw.mat')    # 540 x 3
    
    print np.shape(mat_raw_eeg['data'])
    print np.shape(mat_events_eeg['data'])

    print len(mat_raw_eeg['data'])
