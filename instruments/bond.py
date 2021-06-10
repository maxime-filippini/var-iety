from .instrument import Instrument
from .term_structure import TermStructure, CurveData
from .terms_conditions import TermsConditions
from .timeseries import TimeSeries, TimeSeriesData

from datetime import datetime
from dateutil.relativedelta import relativedelta

import numpy as np
from scipy.optimize import minimize

class Bond(Instrument):
    def __init__(self, 
                 id: str = None, 
                 name: str = None, 
                 currency: str = None,
                 valuation_date: datetime = None,
                 terms_conditions: TermsConditions = TermsConditions(),
                 price: float = None):
        
        super().__init__(id=id, name=name, currency=currency, valuation_date=valuation_date, price=price)
        self.terms_conditions = terms_conditions

    def assign_curves(self, 
                      risk_free_curve: TermStructure = None,
                      spread_curve: TermStructure = None,
                      discount_curve: TermStructure = None,
                      coupon_curve: TermStructure = None):
        
        self.curves = CurveData(
            risk_free=risk_free_curve,
            spread=spread_curve,
            discount=discount_curve,
            coupon=coupon_curve,
        )
        
    def assign_timeseries(self, coupon_rate_timeseries: TimeSeries = None):
        self.timeseries = TimeSeriesData(
            coupon_rate=coupon_rate_timeseries,
        )
        
        
    def compute_discount_rates(self, coupon_days):
        if self.curves.discount:
            discount_rates = self.curves.discount.interpolate(coupon_days)
            
        else:
            if self.curves.risk_free:
                discount_rates = self.curves.risk_free.interpolate(coupon_days)
                
                if self.curves.spread:
                    discount_rates += self.curves.spread.interpolate(coupon_days)
                    
            else:
                raise Exception('No curve supplied!')   
            
        return discount_rates
        
    def add_price(self):
        flat_spread = self.compute_flat_spread()
        
        [self.price, 
         self.coupon_rates, 
         self.cash_flows, 
         self.discounted_cash_flows, 
         self.discount_rates] = self.compute_price(flat_spread=flat_spread)
        
    def build_coupon_schedule(self):
        valuation_date = self.valuation_date
        maturity_date = self.terms_conditions.maturity_date
        frequency = self.terms_conditions.coupon_frequency
        
        coupon_schedule = []
        curr_date = maturity_date
        
        while curr_date > valuation_date:
            coupon_schedule.append(curr_date)
            curr_date = curr_date + relativedelta(months=-1*int(12/frequency))
            
            
        self.terms_conditions.coupon_schedule = coupon_schedule[::-1]   
        
        
        
    def compute_price(self, flat_spread=None):
        if flat_spread is None:
            flat_spread = 0
        
        coupon_dates = np.array(self.terms_conditions.coupon_schedule)
        coupon_days, coupon_years = np.vectorize(lambda x: self.date_difference(self.valuation_date, x, 'ACT/365'))(coupon_dates)        
        
        # 1. Get discount rates
        discount_rates = self.compute_discount_rates(coupon_days) + flat_spread
                
        # 2. Get coupon rates
        if self.terms_conditions.coupon_type == 'fixed':
            coupon_rates = np.repeat(self.terms_conditions.coupon_rate, len(discount_rates))
        else:
            pass
        
        # 3. Compute discounted cash flows
        cash_flows = coupon_rates*100
        cash_flows[-1] += 100
        discounted_cash_flows = cash_flows*np.exp(-discount_rates*coupon_years)
        
        return discounted_cash_flows.sum(), coupon_rates, cash_flows, discounted_cash_flows, discount_rates
    
    def compute_flat_spread(self):
        def loss(flat_spread):
            return abs(self.compute_price(flat_spread=flat_spread)[0] - self.price)
        
        res = minimize(loss, 0.1, tol=1e-9)
        return res.x[0]

        
        
