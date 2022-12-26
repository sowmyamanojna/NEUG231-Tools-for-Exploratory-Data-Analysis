# Cell magic (%%) and Line magic (%)
import numpy as np

def define_filt(freq, filt_freq, type_filt):
    """
    Generate the filter
    Inputs:
        freq: actual set of frequencies
        filt_freq: frequencies that have to be filtered
        type_filt: type pf filter that has to be implemented
    """
    
    if type_filt == "lp":
        lp = filt_freq
        bool_flag = freq <= lp
    elif type_freq == "hp":
        hp = filt_freq
        bool_flag = freq >= hp
    elif type_freq == "band":
        lp,hp = filt_freq
        bool_flag = (freq >= lp) & (freq <= hp)
    else:
        raise ValueError("The filter type should be 'lp', 'hp' or 'band'")
        
    return bool_flag


def apply_filt(sig, filt):
    """
    Fucntion to apply the filter on the signal
    Input:
        sig: The signal
        filt: Filter
    Output: Filtered Signal
    """
    
    cplx = np.fft.rfft(sig)
    
    return np.fft.irfft(cplx * filt)
