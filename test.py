import comms_utils
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    bandwidth = 500000
    tb = 1/bandwidth
    ts = tb*2
    rect = comms_utils.pulse.Sin(ts)
    message_length = 10
    oversampling_factor = 100000
    ak = comms_utils.ak.AK(n=message_length, levels=4)
    # comms_utils.plot.eye_diagram(ak, rect, 100, snr_db=None)
    # print(ak)
    # ak.oversample(1)
    convolved_ak = ak.convolve(rect, oversampling_factor)
    # convolved_ak.add_noise(20)
    ak.oversample(oversampling_factor)
    x = list(np.arange(0, ts*(message_length), ts*message_length/len(convolved_ak)))
    # pulse = [rect[float(i)] for i in np.arange(0, ts, 0.001)]
    # pulse_x = list(np.arange(0, ts, 0.001))
    x2 = list(np.arange(0, ts*(message_length), ts*message_length/len(ak)))
    # print(convolved_ak)
    plot = plt.plot(x, convolved_ak, '-g')
    plot2 = plt.plot(x2, ak, '--r')
    # pulse_plot = plt.plot(pulse_x, pulse, '--b')
    plt.show()
