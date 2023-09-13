#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = {}

  def reset_register_total(self):
    self.total = 0
    
  def add_item(self, title, price, quantity=1):
    self.last_transaction = {"title": title, "price": price, "quantity": quantity}
    self.total += price * quantity
    for i in range(0, quantity):
      self.items.append(title)

  def apply_discount(self):
    if (self.discount > 0):
      self.total -= self.total * (self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if (len(self.items) == 0):
      self.reset_register_total()
      return

    self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
    for i in range(0, self.last_transaction["quantity"]):
      self.items.pop()
    # self.total -= self.last_transaction

register = CashRegister()

register.add_item("eggs", 10, 6)
print(register.total)
register.add_item("ham", 20, 2)
print(register.total)

print("BEFORE LAST TRANSACTION")
print(register.items)

register.void_last_transaction()

print("AFTER LAST TRANSACTION")
print(register.items)
print(register.total)




