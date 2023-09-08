class Stock:
    def __init__(self, symbol: str, name: str, previous_price: float, current_price: float):
        self.__symbol = symbol
        self.__name = name
        self.__previous_price = previous_price
        self.__current_price = current_price

    def getname(self):
        return self.__name

    def getsymbol(self):
        return self.__symbol

    def setprevious_price(self, previousprice : float):
        self.__previous_price = previousprice

    def getprevious_price(self):
        return self.__previous_price

    def setcurrent_price(self, currentprice : float):
        self.__current_price = currentprice

    def getcurrent_price(self):
        return self.__current_price

    def getchangepercent(self):
        change = ((self.__current_price-self.__previous_price)/self.__previous_price)*100
        change_rounded_off="{:.2f}%".format(change)
        return change_rounded_off

stock1 = Stock('INTC', 'Intel Corporation', previous_price=20.5, current_price=20.35)

print(stock1.getchangepercent())

