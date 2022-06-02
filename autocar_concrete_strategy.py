from strategy import Strategy


class AutoCarStrategy(Strategy):
    """
    AutoCar strategy
    """
    def get_route(self, x, y):
        s = set()
        if x > y:
            x, y = y, x
        for route in range(x, y):
            s.add(route)
        print(f"This id set():")
        return s

