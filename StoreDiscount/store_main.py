from StoreDiscount.Plans.annual_plan import AnnualPlan
from StoreDiscount.Plans.half_year_plan import HalfYearPlan
from StoreDiscount.Plans.three_month_plan import ThreeMonthPlan

if __name__ == '__main__':
    print("Абонемент стоит price : 100 000.0 рублей")
    print(f"Подписка со скидкой 10% на 3 месяца: {ThreeMonthPlan().subscription_price} рублей")
    print(f"Подписка со скидкой 20% на полгода: {HalfYearPlan().subscription_price} рублей")
    print(f"Подписка со скидкой 50% + бонус 10000 рублей на 1 год: {AnnualPlan().subscription_price} рублей")
