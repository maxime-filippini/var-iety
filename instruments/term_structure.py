from datetime import datetime
from typing import List
from dataclasses import dataclass, field

from scipy.interpolate import interp1d
import numpy as np

class TermStructure(object):
    def __init__(self,
                  id: str = None, 
                  tenors: List[float] = [],
                  values: list = []):
        self.id = id
        self.tenors = np.array(tenors)
        self.values = np.array(values)
       
    def interpolate(self, new_tenors: List[float], kind='linear'):      
        new_tenors = np.array(new_tenors)        
        f = interp1d(self.tenors, self.values, kind=kind)
        return f(new_tenors)


@dataclass
class CurveData:
    risk_free: TermStructure = field(default=TermStructure())
    spread: TermStructure = field(default=TermStructure())
    discount: TermStructure = field(default=TermStructure())
    coupon: TermStructure = field(default=TermStructure())
