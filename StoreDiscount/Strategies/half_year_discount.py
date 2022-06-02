from StoreDiscount.discount_strategy import DiscountStrategy


class HalfYearDiscount(DiscountStrategy):
    """
    Конкретная реализация стратегии
    Скидка на пол года
    """
    @property
    def percent_off(self) -> int:
        return 20

    