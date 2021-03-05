import math
import random


class Stock(object):
    random_arr = []
    ADD = 1
    CUT = 0
    increaseLoadFactor = 50

    def init_random_arr(self):
        for num in range(1000):
            self.random_arr.append(num % 2)

    def add_random(self, num):
        print(num)
        for num in range(math.ceil(abs(num))):
            if (num > 0):
                self.random_arr.append(Stock.ADD)
                continue
            self.random_arr.append(Stock.CUT)

    def Stud(self, increase, highPrice, nowPrice, masterFunds, bottoMmcad=False, increaseLoadFactor=50):
        print("涨幅: " + str(increase) + "%");
        print("最高价: " + str(highPrice));
        print("现价: " + str(nowPrice));
        print("五日主力流入: " + str(masterFunds) + "亿");
        print("******************************");
        self.init_random_arr()

        print("涨幅基点:")
        self.add_random(increase * increaseLoadFactor)

        print("价格基点:")
        self.add_random((highPrice - nowPrice) / highPrice / 0.05 * increaseLoadFactor)

        print("主力基点:")
        self.add_random(masterFunds * increaseLoadFactor)

        print("底部背离基点:")
        self.add_random(len(self.random_arr) * 0.1 if bottoMmcad else -len(self.random_arr) * 0.1)

        print("******************************")
        add = 0
        cut = 0
        for num in range(100):
            addCut = self.random_arr[random.randint(0, len(self.random_arr))]
            if (addCut == 0):
                cut = cut + 1
                continue
            add = add + 1
        print("******************************")
        print("加仓: " + str(add))
        print("减仓: " + str(cut))
        if(add>cut):
            self.printMore("加仓")
            return
        self.printMore("减仓")

    def printMore(self,str):
        print("******************************")
        print(str)
        print("******************************")


if __name__ == '__main__':
    Stock().Stud(-0.99, 170, 160, -10, True)
