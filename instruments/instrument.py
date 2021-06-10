from datetime import datetime


class Instrument(object):
    def __init__(self, 
                 id=None, 
                 name=None, 
                 currency=None, 
                 valuation_date=None,
                 price=None):
        self.id = id
        self.name = name
        self.currency = currency
        self.valuation_date = valuation_date
        self.price = price
        
    @staticmethod
    def date_difference(date1: datetime, 
                        date2: datetime, 
                        convention: str ='ACT/365') -> float:
        
        D = (date2 - date1).days
        T = D / 365
                
        return D, T