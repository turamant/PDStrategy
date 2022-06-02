from StoreDiscount.discount_strategy import DiscountStrategy


class ThreeMonthDiscount(DiscountStrategy):
    """
    Кокретный класс реализации стратегии
    Скидка на 3 месяца
    """
    @property
    def percent_off(self) -> int:
        return 10
