import comms_utils
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    bandwidth = 0.1
    tb = 1/bandwidth
    ts = tb * 2
    rect = comms_utils.pulse.Rect(ts)
    ak = comms_utils.ak.AK(n=10, levels=16)
    print(ak)
    ak.oversample(1)
    convolved_ak = ak.convolve(rect, 1000)
    convolved_ak.add_noise(20)
    ak.oversample(1000)
    x = list(range(0, len(convolved_ak)))
    pulse = [rect[float(i)] for i in np.arange(0, ts, 0.001)]
    pulse_x = list(np.arange(0, ts, 0.001))
    x2 = list(range(0, len(ak)))
    plot = plt.plot(x, convolved_ak, '-g')
    plot2 = plt.plot(x2, ak, '--r')
    # pulse_plot = plt.plot(pulse_x, pulse, '--b')
    plt.show()
