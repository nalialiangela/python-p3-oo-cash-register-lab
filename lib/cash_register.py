#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, item_name, price, quantity=1):
        for _ in range(quantity):
            self.items.append(item_name)
            self.total += price
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0
        if self.items:
            self.items = self.items[:-1]
  
