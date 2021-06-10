from dataclasses import dataclass, field
from datetime import datetime

from typing import List


@dataclass
class TermsConditions:
    underlying_id: str = field(default='')
    risk_free_curve_id: str = field(default='')
    spread_curve_id: str = field(default='')
    discount_curve_id: str = field(default='')
    coupon_curve_id: str = field(default='')

    maturity_date: datetime = field(default=datetime(1900,1,1))
    coupon_schedule: List[datetime] = field(default_factory=list)
    reset_schedule: List[datetime] = field(default_factory=list)
    daycount_convention: str = field(default='ACT/365')
    coupon_type: str = field(default='Fixed')
    coupon_rate: float = field(default=0)
    coupon_frequency: int = field(default=1)

    strike: float = field(default=None)
    payoff_type: str = field(default='european')
    option_type: str = field(default='call')
    