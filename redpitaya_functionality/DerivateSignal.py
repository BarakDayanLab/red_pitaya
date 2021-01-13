import redpitaya
import numpy as np
sig_derivative = redpitaya.redpitaya()
"duration - the acquired signal length in ms. make sure that the duration is suitable to the task demands."
_,decimation = sig_derivative.acquire(duration=0.001, trigger_source='ch2_negative_edge')
print(decimation)
derivative_non_norm = sig_derivative.derivateInputSig()
sig_derivative.plot(Data=[sig_derivative.derivative.data, sig_derivative.Inputs[0]], Data_0_label = 'Derivative', Data_1_label = 'CH1')

