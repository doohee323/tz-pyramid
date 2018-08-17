import os

class Checkout:
    class Discount:
        def __init__(self, item, price):
            self.item = item
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if cnt >= discount.item:
                    total += self.canCalculateItemDiscountedTotal(item, cnt, discount)
                else:
                    total += self.prices[item] * cnt
            else:
                total += self.prices[item] * cnt
        return total

    def addDiscount(self, item, nitem, price):
        discount = self.Discount(nitem, price)
        self.discounts[item] = discount

    def canCalculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        ndis = cnt / discount.item
        total += ndis * discount.price
        remaining = cnt % discount.item
        total += remaining * self.prices[item]
        return total

    def readPricesFile(self, filename):
        with open(filename) as inFile:
            for line in inFile:
                tokens = line.split()
                self.addItemPrice(tokens[0], int(tokens[1]))
