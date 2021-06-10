from instruments.instrument import Instrument
from instruments.option import Option
from instruments.bond import Bond
from instruments.term_structure import TermStructure
from instruments.terms_conditions import TermsConditions
from instruments.config import Config

from datetime import datetime

cfg = Config()

# terms_conditions = TermsConditions(
#     maturity_date=datetime(2020, 3, 31),
#     strike=100,
#     option_type='call',
#     payoff_type='european'
# )

# valuation_date = datetime(2020,1,31)

# UL = Instrument(price=100)

# TS = TermStructure(tenors=[30, 120], values=[0.01, 0.02])

# O = Option(valuation_date=valuation_date, terms_conditions=terms_conditions, underlying=UL)
# O.assign_curves(discount_curve=TS)
# O.assign_market_variables(volatility=0.2, dividend_yield=0, premium=3)

# print('Black Scholes IV for Option price of 3:')
# print(O.black_scholes_iv())
# print('Black Scholes price for IV of 17.8859066%:')
# print(O.black_scholes_price(sigma=0.17885906682465805))


terms_conditions = TermsConditions(
    maturity_date=datetime(2020, 3, 31),
    coupon_schedule=[datetime(2020, 1, 31), datetime(2020, 2, 28), datetime(2020, 3, 31)],
    coupon_type='fixed',
    coupon_rate=0.05,
)

valuation_date = datetime(2020,1,10)

discount = TermStructure(tenors=[1, 120], values=[0.02, 0.02])
riskfree = TermStructure(tenors=[1, 120], values=[0.01, 0.01])
spread = TermStructure(tenors=[1, 120], values=[0.03, 0.03])

B = Bond(valuation_date=valuation_date, terms_conditions=terms_conditions, price=110)

B.assign_curves(discount_curve=discount, risk_free_curve=riskfree, spread_curve=spread)

all_bonds = [B]*50

for b in all_bonds:
    b.add_price()
    print(b.discounted_cash_flows)