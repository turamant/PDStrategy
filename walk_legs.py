from strategy import Strategy


class WalkLegs(Strategy):
    """
        Walk strategy
    """
    def get_route(self, x, y):
        mapa = dict()
        if x > y:
            x, y = y, x
        for i in range(x, y):
            mapa[i] = y-i
        print(f"This id dict()")
        return mapa
