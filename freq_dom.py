# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import comms_utils


bandwidth = 5
tb = 1/bandwidth
ts = tb*2
rect = comms_utils.pulse.Sinc(ts)
rect.set_max_pulses(20)
message_length = 10
oversampling_factor = 8
ak = comms_utils.ak.AK(n=message_length, levels=4)
comb = comms_utils.comb.Comb(ak, ts*4, oversampling_factor)
signal = comb.convolve(rect)
# signal.add_noise(1)
# signal.plot()
sig_data, sig_time = signal.get_data()
# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = sig_time
y = sig_data
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), 300)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()