from .instrument import Instrument
from .terms_conditions import TermsConditions
from .term_structure import TermStructure, CurveData

from math import log, sqrt, exp
from datetime import datetime

from scipy.stats import norm
from scipy.optimize import minimize

class Option(Instrument):
    def __init__(self, 
                 id: str = None, 
                 name: str = None, 
                 currency: str = None,
                 valuation_date: datetime = None,
                 underlying = None,
                 terms_conditions: TermsConditions = TermsConditions()):
        
        super().__init__(id=id, name=name, currency=currency, valuation_date=valuation_date)
        self.terms_conditions = terms_conditions
        self.underlying = underlying
        
    def assign_curves(self, discount_curve: TermStructure):
        self.curves = CurveData(discount=discount_curve)
        
    def assign_market_variables(self, volatility=None, premium=None, dividend_yield=None):
        self.volatility = volatility
        self.premium = premium
        self.dividend_yield = dividend_yield
        
    def add_price(self):
        if self.option_type == 'european':
            self.
        
    def black_scholes_price(self, sigma=None):
        if sigma is None:
            sigma = self.volatility
        
        S = self.underlying.price
        K = self.terms_conditions.strike
        q = self.dividend_yield
        D, T = self.date_difference(self.valuation_date, 
                                    self.terms_conditions.maturity_date, 
                                    self.terms_conditions.daycount_convention)
        r = self.curves.discount.interpolate([D])[0]
        
        if self.terms_conditions.option_type == 'call':
            return S*exp(-1*q*T)*norm.cdf(self.d1(S, K, r, q, T, sigma))-K*exp(-1*r*T)*norm.cdf(self.d2(S,K,r,q,T,sigma))
        else:
            return K*exp(-1*r*T)*norm.cdf(-1*self.d2(S,K,r,q,T,sigma))-S*exp(-1*q*T)*norm.cdf(-1*self.d1(S, K, r, q, T, sigma))
        
    def black_scholes_iv(self):
        def loss(sigma):
            return abs(self.black_scholes_price(sigma=sigma) - self.premium)
        
        res = minimize(loss, 0.1, tol=1e-9)
        return res.x[0]
        
    @staticmethod
    def d1(S, K, r, q, T, sigma):
        return (log(S/K) + (r-q+0.5*sigma**2)*T)/(sigma*sqrt(T))
    
    @staticmethod
    def d2(S, K, r, q, T, sigma):
        return Option.d1(S, K, r, q, T, sigma)-sigma*sqrt(T)
    

