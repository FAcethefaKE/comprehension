"""
    DICTIONARY COMPREHENSION
(is an elegant and concise way to create dictionaries)

      key value pair       variable in     python object
    you want to create    the iterable     you can loop over

    { key: value          for vars       in iterable }
"""

# squares = {num: num**2 for num in [1, 2, 3, 4, 5]}
# print(squares)
#
# squares = {}
# for num in range(1, 6):
#     squares[num] = num*num
# print(squares)

###
price = {'milk': 1.8, 'coffee': 2.5, 'bread': 2.3}
eur_to_dollar = 1.09

# dollar_price = {item: round((value * eur_to_dollar), 2) for (item, value) in price.items()}
#
# print(dollar_price)


""" with If conditional """
original_dict = {'jack': 18, 'michael': 48, 'tom': 27, 'john': 36}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0 if v > 40}
# print(even_dict)


""" with If Else """
original_dict = {'jack': 18, 'michael': 48, 'tom': 27, 'john': 36}

young_old = {key: ('young' if value < 30 else 'old') for (key, value) in original_dict.items()}
# print(young_old)


""" remove selected item """
category = {'Electronics': 'TV', 'Electronics': 'Laptop', 'Clothing': 'Tshirt',
           'Grocery': 'Vegetables', 'Toys': 'Remote Car', 'Electronics': 'Mobile'}

new_dict = {item: category[item] for item in category.keys() - {'Electronics'}}
# print(new_dict)


""" use of zip function - to zip together two lists """

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

weekly_temp = {day: temp for (day, temp) in zip(days, temp_C)}
print(weekly_temp)


weekly_temp = {}
for day, temp in zip(days, temp_C):
    weekly_temp[day] = temp
print(weekly_temp)


""" 
Even though dictionary comprehensions are is easy to read, they are not always the right choice.
- They can sometimes make the code run slower and consume more memory
- They can also decrease the readability of the code
"""