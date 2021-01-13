
"""
Created on Tue Dec 22 13:33:34 2020

@author: Jeremy and Assaf
this module has the basic functionality of redpitaya.
"""
from matplotlib import pyplot as plt
from pyrpl import Pyrpl
import time
import numpy as np
import SCPIControl

class redpitaya:
    # decimation - he rate at which the memory is filled is the sampling rate (125 MHz) divided by the value of ‘decimation’.
    def __init__(self, gui=False):
        self.HOSTNAME = "rp-f0629e.local"
        self.p = Pyrpl(hostname=self.HOSTNAME,
                       config="C:\\Users\\Jeremy\\pyrpl_user_dir\\config\\global_config.yml", gui=False)
        if gui:
            self.p.show_gui()
        self.r = self.p.rp
        self.s = self.r.scope
        self.s.trigger_delay = 0
        self.s.threshold = 0

    def acquire(self, decimation=1024.0, duration=0.001, trigger_source='ch2_positive_edge', input1 ='in1', input2 ='in2'):
        """
        this function acquires signal of two fast analog inputs of the scope
        :param decimation: the decimation on sampling. decimation=1 is equivalent to 124 MHz of sampling.
                 be aware that the minimal decimation would change as a function of the duration.
        :param duration: the duration of the acquisition in [s]. for triggered signal make sure its as the duration between triggers.
        :param trigger_source: the source for triggering the input signal acquired
        :param input1: the input to channel 1 of the scope
        :param input2: the input to channel 2 of the scope
        :return:
        """
        self.s.decimation = decimation
        self.s.duration = duration
        self.s.input1 = input1
        self.s.input2 = input2
        self.s.trigger_source = trigger_source
        self.res = self.s.curve_async()
        self.Inputs = self.res.await_result()
        return self.res, self.s.decimation
    # Data - two elements to be plotted

    def plot(self, Data, Data_0_label,  Data_1_label ):
        while not self.s.curve_ready(): pass
        # self.ch1, self.ch2 = self.res.await_result()
        plt.clf()
        plt.plot(self.s.times * 1e3, Data[0], '.-', label=Data_0_label)
        plt.plot(self.s.times * 1e3, Data[1], '.-', label=Data_1_label)
        plt.legend()
        plt.xlabel("Time [ms]")
        plt.ylabel("Voltage")
        "derivate an input signal and spit it into one of the outputs"

    def derivateInputSig(self, InputChannel=0):
        derivative_non_norm = np.gradient(self.Inputs[InputChannel], self.s.sampling_time * (self.s.decimation))
        self.derivative.data = derivative_non_norm / (max(derivative_non_norm))
        return self.derivative.data

    def TransmitASG(self, OutputChannel='out1',frequency = 5e2, trigger_source = 'ext_negative_edge'):
        self.derivative = self.r.asg1
        self.derivative.output_direct = OutputChannel
        self.derivative.trigger_source = trigger_source
        self.derivative.frequency = frequency

    def movingaverage(self, interval, window_size):
        window = np.ones(int(window_size)) / float(window_size)
        return np.convolve(interval, window, 'same')