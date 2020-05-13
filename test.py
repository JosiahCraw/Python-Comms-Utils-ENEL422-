import comms_utils
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    bandwidth = 1
    tb = 1/bandwidth
    ts = tb*2
    rect = comms_utils.pulse.Niquist(ts, 1)
    rect.set_max_pulses(10)
    message_length = 5000
    oversampling_factor = 8
    ak = comms_utils.ak.AK(n=message_length, levels=2)
        
    comb = comms_utils.comb.Comb(ak, ts, oversampling_factor)
    signal = comb.pulse_shape(rect, plot_pre_sum=False)
    signal.add_noise(10)
    # signal.plot()
    comms_utils.plot.eye_diagram(signal, rect, comb.get_clock_comb())
    # signal.add_noise(2)
    # signal.plot()
    sig_data, sig_time = signal.get_data()
    # comms_utils.plot.eye_diagram(ak, rect, oversampling_factor, snr_db=10)
    ak.oversample(oversampling_factor)
    # x = list(np.arange(0, ts*(message_length), ts*message_length/len(convolved_ak)))
    # pulse = [rect[float(i)] for i in np.arange(0, ts, ts/pulse_sample_points)]
    num_periods = 10
    pulse = rect.get_num_pulses(oversampling_factor, num_periods)
    pulse_x = rect.get_pulse_times(oversampling_factor, num_periods)
    # x2 = list(np.arange(0, ts*(message_length), ts*message_length/len(ak)))
    # print(convolved_ak)
    # plot = plt.plot(pulse_x, pulse, '-g')
    true_data = ak.get_data()
    # x = [i for i in range(len())]
    true_data = rect.apply_conv_delay(len(sig_data), true_data)

    comb_data = rect.apply_conv_delay(len(sig_data), comb.get_clock_comb())
    plot2 = plt.plot(sig_time, true_data, '--r')
    pulse_plot = plt.plot(sig_time, sig_data, '-b')
    # print(comms_utils.decode.decode_pam(signal*comb_data, ak.get_levels()))
    plt.show()
