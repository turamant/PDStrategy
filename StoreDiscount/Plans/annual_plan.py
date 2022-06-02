from StoreDiscount.Strategies.annual_discount import AnnualDiscount
from StoreDiscount.plan import Plan


class AnnualPlan(Plan):
    def __init__(self):
        super().__init__(AnnualDiscount())
