"""
The Nile
The Nile fullfilment agency brings everything you could possibly want straight
 to your door! Use your knowledge of Python functions and how to manipulate arguments
   to help automate practices for the biggest world-changing company.

If you need help during this project, check out the project walkthrough
 video which can be found in the Get Unstuck menu.

1. At The Nile our biggest concern is our consumers, and our biggest cost is
 delivering their goods to them. We want to develop a program that will help us
   minimize these costs so we can continue making everyone happy.

First well need to calculate these costs using a function
 that youre going to write called calculate_shipping_cost().

Give calculate_shipping_cost three parameters: from_coords,
 to_coords, and shipping_type.

2. Both from_coords and to_coords are tuples, containing first the
 latitude and then the longitude. Since our get_distance() function looks
   for all four as separate arguments, well need to separate these variables out.

Inside calculate_shipping_cost unpack those tuples into from_lat,
 from_long, to_lat, and to_long.

3. Now call get_distance(from_lat, from_long, to_lat, to_long) and save the result 
as distance.

Theres other ways to separate those two coordinates
 when calling this function, how would you have done it?

4. Next, get the shipping_rate by using the provided SHIPPING_PRICES
 dictionary and fetching the key passed in as shipping_type

5. Calculate the price by multiplying the distance by the shipping_rate.

6. Finally, return the formatted price, created by calling the provided format_price()
 on the price itself.

7. What about our shoppers who hastily purchase goods without indicating their 
shipping type? Lets give our function a default argument for shipping_type. 
Since theyre in such a hurry lets make the default argument 'Overnight'. 
Theyll be happier to get what they ordered earlier, 
and well be happier because they paid more money for it. Its a win-win!

8. Want to make sure you wrote the function correctly? 
Try calling test_function(calculate_shipping_cost) after your function definition.

"""
# code located in nile.py 

from math import sin, cos, atan2, sqrt

def get_distance(from_lat, from_long, to_lat, to_long):
  dlon = to_long - from_long
  dlat = from_lat - to_lat
  a = (sin(dlat/2)) ** 2 + cos(from_lat) * cos(to_lat) * (sin(dlon/2)) ** 2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  distance = a * c
  return distance

SHIPPING_PRICES = {
  'Ground': 1,
  'Priority': 1.6,
  'Overnight': 2.3,
}

def format_price(price):
  return "${0:.2f}".format(price)


# code located in script.py
#from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords,shipping_type='Overnight'):
   # Check if shipping_type is provided, otherwise set default
   from_lat, from_long = from_coords
   to_lat, to_long = to_coords
   distance = get_distance(from_lat, from_long,to_lat, to_long)
   shipping_rate = SHIPPING_PRICES[shipping_type] 
   price = distance*shipping_rate
   return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None

    for driver in drivers:
        driver_time = distance / driver.speed
        price_for_driver = driver.salary * driver_time

        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver

    return cheapest_driver_price, cheapest_driver



# Test the function by calling 
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
    total_money_made = 0
    
    for trip_id, trip in trips.items():
        trip_revenue = trip.cost - trip.driver.cost
        total_money_made += trip_revenue
    
    return total_money_made


# Test the function by calling 
test_function(calculate_money_made)
