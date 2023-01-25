import unittest
import alerts_errors


# ________ Exceptions
# exceptions are runtime errors
# number = 10
# if number >= 0:
#     print("yey")
# else:
#     raise Exception("wrong! Number is not grater than 10")

# __________ we can handle multiple exceptions:

# try:
#     # Some code to try!
# except (NameError, ZeroDivisionError) as e:
#     print('We hit an Exception!')
#     print(e)

# - we can also use multiple exceptions
# - multiple exceptions
# instrument_prices = {
#   'Banjo': 200,
#   'Cello': 1000,
#   'Flute': 100,
# }
#
# def display_discounted_price(instrument, discount):
#   full_price = instrument_prices[instrument]
#   discount_percentage = discount / 100
#   discounted_price = full_price - (full_price * discount_percentage)
#   print("The instrument's discounted price is: " + str(discounted_price))
#
# instrument = 'Banjo'
# discount = '20'
#
# # Write your code below:
# try:
#     display_discounted_price(instrument, discount)
# except KeyError:
#     print("An invalid instrument was entered!")
# except TypeError:
#     print("Discount percentage must be a number!")
# except Exception:
#     print("Hit any other exception")


# ------------ else cause in try except block of code
# customer_rewards = {
#   'Zoltan': 82570,
#   'Guadalupe': 29850,
#   'Mario': 17849
# }
#
# def display_rewards_account(customer):
#   try:
#       rewards_number = customer_rewards[customer]
#   except KeyError:
#       print("Customer was not found in rewards program!")
#   else:
#       print('Rewards account number is: ' + str(rewards_number))
#
#
# customer = 'Mario'
# display_rewards_account(customer)


# __________ Customizing User-defined Exceptions
# Write your code below (Checkpoint 1 & 2)
# class InventoryError(Exception):
#   def __init__(self, supply):
#     self.supply = supply
#   def __str__(self):
#     return 'Available supply is only ' + str(self.supply)
#
# inventory = {
#   'Piano': 3,
#   'Lute': 1,
#   'Sitar': 2
# }
#
# def submit_order(instrument, quantity):
#   supply = inventory[instrument]
#   if quantity > supply:
#     raise InventoryError(supply)
#   else:
#     inventory[instrument] -= quantity
#     print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))
#
# instrument = 'Piano'
# quantity = 5
# submit_order(instrument, quantity)


# -------- unit testing propriu-zis

def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location


# Write your code below:
def test_row_1(func):
    assert func(1) == 'front', 'The nearest exit to row 1 is in the front!'


def test_row_20(func):
    assert func(20) == "middle", 'The nearest exit to row 20 is in the middle!'


def test_row_40(func):
    assert func(40) == 'back', 'The nearest exit to row 40 is in the back!'


test_row_1(get_nearest_exit)
test_row_20(get_nearest_exit)
test_row_40(get_nearest_exit)


class SystemAlertTests(unittest.TestCase):
    def test_power_outage_alert(self):
        self.assertRaises(alerts_errors.PowerError, alerts_errors.power_outage_detected, True)

    def test_water_levels_warning(self):
        self.assertWarns(alerts_errors.WaterLevelWarning, alerts_errors.water_levels_check, 150)

unittest.main()