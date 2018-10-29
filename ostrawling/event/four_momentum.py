import numpy as np

class FourMomentum:
    def __init__(self, px,py,pz,m=None, e=None):
        if m is not None and e is not None:
            raise ValueError('Please set one of energy or mass when creating a four-momenta.' )

        self._px = px
        self._py = py
        self._pz = pz

        self.space_like = True
        if m is None and e is not None:
            mag = np.abs(self.p()**2-e**2)
            m = np.sqrt(mag)
            self.space_like = (self.p()**2<e**2)

        self._m = m

    def eta(self):
        return 0.5*np.log( (self.p()+self.pz())/(self.p()-self.pz())  )

    def p(self):
        return np.sqrt(self.px()**2 + self.py()**2 + self.pz()**2)

    def e(self):
        return np.sqrt(self.m()**2 + self.p()**2 )

    def pt(self):
        return np.sqrt(self.px()**2 + self.py()**2)

    def px(self):
        return self._px

    def py(self):
        return self._py
        
    def pz(self):
        return self._pz
        
    def m(self):
        return self._m

    def theta(self):
        return np.arccos(self.pz()/self.p())

    def phi(self):
        return np.arctan(self.py()/self.px())


    def __add__(self, b):
        """
        Define the result of self + b, where b is a four momenta
        """
        assert(isinstance(b, FourMomentum), 'Addition between four momenta requires both classes to be a four momenta object.')
        res = FourMomentum(px=self.px() + b.px(),
                py=self.py() + b.py(),
                pz=self.pz() + b.pz(),
                e=self.e() + b.e(),
            )
        return res
        
