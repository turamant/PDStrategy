from StoreDiscount.Strategies.three_month_discount import ThreeMonthDiscount
from StoreDiscount.plan import Plan


class ThreeMonthPlan(Plan):
    def __init__(self):
        super().__init__(ThreeMonthDiscount())
