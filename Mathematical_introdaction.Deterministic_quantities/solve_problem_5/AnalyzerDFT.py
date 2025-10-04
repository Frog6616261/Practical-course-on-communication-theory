import numpy as np

pi = np.pi

class AnalyzerDFT:

    def __init__(self, freq_disc, func, start_t, end_t):
        if (end_t < start_t): print("error")
        if (freq_disc <= 0): print("error")

        self._freq_disc     = np.double(freq_disc)
        self._freq_Na       = self._freq_disc / 2
        self._func          = func  
        self._dt            = np.double(1/freq_disc)
        self._start_t       = np.double(start_t)
        self._end_t         = np.double(end_t)
        self._N             = np.int64(np.floor((end_t - start_t)/self._dt) + 1)
        self._dw            =  self._freq_disc / self._N
        self._w_arr         = np.arange(self._N) * self._dw     
        self._signal_arr    = self._generate_signal()
        self._spec          = self._compute_dft()
        self._amp_spec      = self._compute_amp()
        self._phase_spec    = self._compute_phase()
        self._time_arr      = np.arange(self._N) * self._dt + self._start_t   

     

    def _generate_signal(self):
        t = np.arange(self._N) * self._dt + self._start_t
        return self._func(t)
    
    def _compute_dft(self):
        func_val = self._generate_signal()
        spec = np.arange(self._N)*0j
        
        for k in np.arange(self._N):
            for val_num in np.arange(self._N):
                lol = func_val[val_num] * np.exp(-1j * (2*pi*k*val_num) / (self._N))
                spec[k] += lol

        return spec        
    
    def _compute_amp(self):
        spectrum = self._compute_dft()
        return np.abs(spectrum)
    

    def _compute_phase(self):
        spectrum = self._compute_dft()
        return np.angle(spectrum)
    
