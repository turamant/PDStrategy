from decimal import Decimal

from StoreDiscount.discount_strategy import DiscountStrategy


class AnnualDiscount(DiscountStrategy):
    """
    Конкретный класс реализации стратегии

    Скидка за год.
    Кроме процентной скидки дарим в подарок скидку в 10 000 рублей.
    """
    @property
    def percent_off(self) -> int:
        return 50

    @property
    def money_off(self):
        return 10000

    def calculate_discounted_price(self, price) -> Decimal:
        return super().calculate_discounted_price(price) - self.money_off
