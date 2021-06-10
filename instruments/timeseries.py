from dataclasses import dataclass, field

import numpy as np

class TimeSeries(object):
    def __init__(self, dates: np.ndarray = None, levels: np.ndarray = None):
        self.dates = dates
        self.levels = levels
        
@dataclass
class TimeSeriesData():
    coupon: TimeSeries = field(default=TimeSeries()) 
    underlying_spot: TimeSeries = field(default=TimeSeries()) 
       