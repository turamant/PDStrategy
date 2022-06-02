from strategy import Strategy


class PublicTransport(Strategy):
    """
        PublicTransport strategy
    """
    def get_route(self, x, y):
        lis = list()
        if x > y:
            x, y = y, x
        for i in range(x, y):
            lis.append(i)
        print(f"This id list():")
        return lis
