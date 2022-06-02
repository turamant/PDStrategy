from autocar_concrete_strategy import AutoCarStrategy
from strategy import Strategy


class Context:
    def __init__(self, strategy: Strategy = AutoCarStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def execute_strategy(self, x, y):
        return self.strategy.get_route(x, y)
