import numpy as np

class FourMomentum:
    def __init__(self, vec, basis='x,y,z,m'):
        self.set_basis(vec,basis)

    def set_basis(self, vec, basis='x,y,z,m'):
        """
        @brief Set the four-momentum where vec is a four vector in the basis defined by
        the string basis, e.g 'xyzm' corresponds to cartesian where the fourth

        @params 
        vec: A list/tuple of four numbers
        basis: a string defining the basis the four numbers are  based in
        """
        basis = basis.lower()
        if basis == 'x,y,z,m':
            self._px = vec[0]
            self._py = vec[1]
            self._pz = vec[2]
            self._m = vec[3]
        elif basis == 'x,y,z,e':
            self._px = vec[0]
            self._py = vec[1]
            self._pz = vec[2]
            e = vec[3]
            mag = np.abs(self.p**2-e**2)
            self._m = mag * np.sign(self.p**2-e**2)
        elif basis == 'pt,eta,phi,m':
            self._px = vec[0]*np.cos(vec[2])
            self._py = vec[0]*np.sin(vec[2])
            self._pz = vec[0]*np.sinh(vec[1])
            self._m = vec[3]
        elif basis == 'pt,eta,phi,e':
            self._px = vec[0]*np.cos(vec[2])
            self._py = vec[0]*np.sin(vec[2])
            self._pz = vec[0]*np.sinh(vec[1])
            e = vec[3]
            self._m = mag * np.sign(self.p**2-vec[3]**2)

        elif basis == 'p,theta,phi,m':
            self._px = vec[0]*np.cos(vec[2])
            self._py = vec[0]*np.sin(vec[2])
            self._pz = vec[0]*np.sinh(vec[1])
            self._m = vec[3]
            
        elif basis == 'p,theta,phi,e':
            self._px = vec[0]*np.sin(vec[1])*np.cos(vec[2])
            self._py = vec[0]*np.sin(vec[1])*np.sin(vec[2])
            self._pz = vec[0]*np.cos(vec[1])
            e = vec[3]
            self._m = mag * np.sign(self.p**2-vec[3]**2)

        else:
            raise ValueError(' Basis %s is not one of the supported options. It must be "xyzm", "xyze", "pTEtaPhiE", "pTEtaPhiE"'%(basis))

    @property
    def eta(self):
        return 0.5*np.log( (self.p+self.pz)/(self.p-self.pz)  )

    @property
    def p(self):
        return np.sqrt(self.px**2 + self.py**2 + self.pz**2)

    @property
    def e(self):
        return np.sqrt(self.m**2 + self.p**2 )

    @property
    def pt(self):
        return np.sqrt(self.px**2 + self.py**2)

    @property
    def px(self):
        return self._px

    @property
    def py(self):
        return self._py
        
    @property
    def pz(self):
        return self._pz

    @property
    def m(self):
        return self._m

    @property
    def theta(self):
        return np.arccos(self.pz/self.p)

    @property
    def z(self):
        return self.pz/self.p

    @property
    def phi(self):
        return np.arctan(self.py/self.px)

    @property
    def beta(self):
        return self.p/self.e
    
    def __add__(self, b):
        """
        Define the result of self + b, where b is a four momenta
        """
        res = FourMomentum(
                (self.px + b.px,
                self.py + b.py,
                self.pz + b.pz,
                self.e + b.e),
                'x,y,z,e'
            )
        return res
        
