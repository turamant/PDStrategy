from abc import ABC, abstractmethod
from decimal import Decimal


class DiscountStrategy(ABC):
    """Абстрактный класс стратегии
    """

    @property
    @abstractmethod
    def percent_off(self) -> int:
        pass

    def calculate_discounted_price(self, price) -> Decimal:
        """
        Калькуляция скидки от процента
        :param price:
        :return: Decimal
        """
        return price - price * self.percent_off / 100
