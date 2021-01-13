"""
1.
Let's assume you are planning to use your Python skills to build a social networking service.
You decide to host your application on servers running in the cloud. You pick a hosting provider
that charges $0.51 per hour. You will launch your service using one server and want to know
how much it will cost to operate per day and per month.
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
"""
charge_per_hour = 0.51
charge_per_day = charge_per_hour * 24
charge_per_month = charge_per_day * 30
print('Cost of operation for a day: $' + str(charge_per_day))
print('Cost of operation for a month: $' + str(charge_per_month))


"""
2.
Building on the previous example, let's also assume that you have saved $918 to fund your new
adventure. You wonder how many days you can keep one server running before your money
runs out. Of course, you hope your social network becomes popular and requires 20 servers to
keep up with the demand. How much will it cost to operate at that point?
Write a Python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per month?
How much does it cost to operate twenty servers per day?
How much does it cost to operate twenty servers per month?
How many days can I operate one server with $918?
"""
cost_of_20s_per_day = charge_per_day * 20
cost_of_20s_per_month = cost_of_20s_per_day * 30
savings = 918
days_of_operation = savings / charge_per_day
print('Cost of runnning 20 servers for a day: $' + str(cost_of_20s_per_day))
print('Cost of running 20 servers for a month: $' + str(cost_of_20s_per_month))
print('For many days we can operate a server for $' + str(savings) + ': ' + str(days_of_operation))