from StoreDiscount.Strategies.half_year_discount import HalfYearDiscount
from StoreDiscount.plan import Plan


class HalfYearPlan(Plan):
    def __init__(self):
        super().__init__(HalfYearDiscount())
