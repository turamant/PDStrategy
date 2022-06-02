from public_transport import PublicTransport
from walk_legs import WalkLegs
from autocar_concrete_strategy import AutoCarStrategy
from bicycle_strategy import BiCycle
from context import Context

if __name__ == '__main__':
    context = Context()

    operand = str(input("Введите(выберите из: <Car, Walk, Autobus, Bicycle) операнд: \n"))
    argX = int(input("Введите значение X: "))
    argY = int(input("Введите значение Y: "))

    if operand == "Car":
        context.set_strategy(AutoCarStrategy())

    if operand == "Walk":
        context.set_strategy(WalkLegs())

    if operand == "Autobus":
        context.set_strategy(PublicTransport())

    if operand == "Bicycle":
        context.set_strategy(BiCycle())

    result = context.execute_strategy(argX, argY)
    print("Point of coordinats: ", result)

