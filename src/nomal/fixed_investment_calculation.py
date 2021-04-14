def get():
    pass


def get2(years, monthMoney, rate):
    rate = rate / 12
    money = monthMoney
    for year in range(years):
        for m in range(12):
            money = (money + monthMoney) * (1 + rate)
            print("第 %s 月: 总余额: %s" % (str(m + 1), str(money)))

if __name__ == '__main__':
    get2(2, 1000, 0.1)
