#!/usr/bin/python

import sys
import redpitaya_scpi as scpi
# Created By Assaf Shonfeld
# 29.12.2020
# this class includes all the SCPI functions needed for the control of the redpitaya
class SCPIControl:
   def SigAcqTrig(self,wave_form='sine', freq=1e4, ampl=1):
    r"""

    This example shows how to acquire 16k samples of signal on fast analog inputs.
    Signal will be acquired when the external trigger condition is meet. Time length of the acquired
    signal depends on the time scale of a buffer that can be set with a decimation factor.

    Parameters
    ----------

    Returns
    -------

    Other Parameters
    ----------------

    Raises
    ------

    See Also
    --------

    Notes
    -----


    References
    ----------

    Examples
    --------
    """
    rp_s = scpi.scpi('169.254.43.77')

    rp_s.tx_txt('GEN:RST')
    rp_s.tx_txt('SOUR1:FUNC ' + str(wave_form).upper())
    rp_s.tx_txt('SOUR1:FREQ:FIX ' + str(freq))
    rp_s.tx_txt('SOUR1:VOLT ' + str(ampl))
    # rp_s.tx_txt('SOUR1:BURS:NCYC 10000')
    # rp_s.tx_txt('SOUR1:BURS:STAT ON')
    # rp_s.tx_txt('SOUR1:TRIG:SOUR OUT1')
    # rp_s.tx_txt('SOUR1:TRIG:IMM')
    rp_s.tx_txt('OUTPUT1:STATE ON')

if __name__ == '__main__':
  a = SCPIControl()
  a.SigAcqTrig()