def getMoneyHasYear(expectedMoney, monthMoney, rate):
    print("达到余额%s万元\t\t每月定投: %s元\t\t\t年利率: %s" % (str(expectedMoney), str(monthMoney), str(rate)))
    money = 0
    year = 0
    yearMoney = monthMoney * 12
    while True:
        lastYearMoney = money;
        money = (money + monthMoney * 12) * (1 + rate)
        if year == 0:
            lastYearMoney = yearMoney
            currentIncome = (money - lastYearMoney) / 10000
        else:
            currentIncome = (money - lastYearMoney - yearMoney) / 10000

        print("第 %s 年:  \t\t当年收益: %s(万元)\t\t\t总余额: %s（万元）" % (
            str(year + 1), str(round(currentIncome, 2)), str(round(money / 10000, 2))))
        year = year + 1
        if money >= expectedMoney * 10000:
            investmentMoney = year * monthMoney * 12
            print("第%s年,余额超过%s(万元),累计投入: %s(万元),累计收益%s(万元)" % (str(year), str(expectedMoney),str(round(investmentMoney/10000,2)),str(round((money-investmentMoney)/10000,2))))
            break


def fixedByMonth(years, monthMoney, rate):
    print("累计定投%s年\t\t每月定投: %s元\t\t\t年利率: %s" % (str(years), str(monthMoney), str(rate)))
    yearMoney = monthMoney * 12
    money = 0
    lastYearMoney = 0;
    for year in range(years):
        lastYearMoney = money;
        money = (money + yearMoney) * (1 + rate)
        if year == 0:
            lastYearMoney = yearMoney
            currentIncome = (money - lastYearMoney) / 10000
        else:
            currentIncome = (money - lastYearMoney - yearMoney) / 10000

        print("第 %s 年:  \t\t当年收益: %s(万元)\t\t\t总余额: %s（万元）" % (str(year + 1), str(round(currentIncome, 2)), str(round(money / 10000, 2))))

    investmentMoney = year * monthMoney * 12

    print("累计投入: %s(万元),累计收益%s(万元)" % (str(round(investmentMoney/10000, 2)), str(round((money - investmentMoney) / 10000, 2))))


if __name__ == '__main__':
    fixedByMonth(20, 4000, 0.13)
    print("##################################")
    # getMoneyHasYear(100, 4000, 0.15)
