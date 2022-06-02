from strategy import Strategy


class BiCycle(Strategy):
    """
    Bicycle strategy
    """
    def get_route(self, x, y):
        if x > y:
            print("This is выражение - генератор")
            t = (route for route in range(x, y, -1))
            return list(t)
        print("This is list comprehensive")
        return [route for route in range(x, y)]
