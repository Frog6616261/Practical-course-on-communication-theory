import numpy as np


SEED_CONST = np.uint32(17)
A_CONST = np.uint32(1664525)
C_CONST = np.uint32(1013904223)
M_CONST = np.uint64(2**32)

class UniformGenerator:
    
    def __init__(self, seed=None, a=None, c=None, m=None):
        self._seed       = np.uint32(seed) if (seed is not None) else  SEED_CONST
        self._a          = np.uint32(a) if (a is not None) else A_CONST
        self._c          = np.uint32(c) if (c is not None) else C_CONST
        self._m          = np.uint64(m) if (m is not None) else M_CONST
        self._cur_sample = self._seed
    
    def _get_next_sample(self):
        self._cur_sample = (self._a *self._cur_sample + self._c) % self._m

        return self._cur_sample / self._m


    def generate_samples(self, n):
        samples = np.empty(n, dtype=np.float64)
        
        for i in range(n):
            samples[i] = self._get_next_sample()

        return samples

    def reset(self, seed=None):
        self._seed = np.uint32(seed) if (seed is not None) else self._seed
        self._cur_sample = np.uint32(seed) if (seed is not None) else self._seed
