from StoreDiscount.discount_strategy import DiscountStrategy


class Plan:
    """
    Контекст определяет интерфейс, представляющий интерес для клиентов
    План подписки.
    """
    price = 100000   # базовая цена подриски

    def __init__(self, discount: DiscountStrategy):
        """
        Контекст либо принимает стратегию через конструктор, либо
        предоставляет сеттер для её изменения вво время выполнения.
        :param discount:
        """
        self._discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount: DiscountStrategy):
        self._discount = discount

    @property
    def subscription_price(self):
        return self.discount.calculate_discounted_price(self.price)