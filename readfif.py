import mne
import matplotlib.pyplot as plt

mne.set_log_level('INFO')


raw = mne.io.read_raw_fif('MIIR_dataset/P01-raw.fif')
print(raw)
print(raw.info['ch_names'])

# start, stop = raw.time_as_index([100, 115])  # 100 s to 115 s data segment
# data, times = raw[:, start:stop]
# print(data.shape)
# print(times.shape)
# data, times = raw[2:20:3, start:stop]  # access underlying data
for i in range(len(raw.info['ch_names'])):
	events = mne.find_events(raw,stim_channel=raw.info['ch_names'][i])
	print events

# raw.plot(block=True),