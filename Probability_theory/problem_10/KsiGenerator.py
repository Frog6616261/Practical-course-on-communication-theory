import numpy as np
from UniformGenerator import UniformGenerator


LM_CONST = np.float64(1)

class KsiGenerator:
    
    def __init__(self, lm=None, seed=None, a=None, c=None, m=None):
        self._lm        = np.float64(lm) if (lm is not None) else  LM_CONST
        self._uni_gen   = UniformGenerator(seed, a, c, m)
    
    def _get_next_sample(self):
        k = self._uni_gen._get_next_sample()

        return (1/self._lm)*(np.log(k) - np.log(1 - k))


    def generate_samples(self, n):
        samples = np.empty(n, dtype=np.float64)
        
        for i in range(n):
            samples[i] = self._get_next_sample()

        return samples

    def reset(self, seed=None):
        self._uni_gen.reset(seed)
