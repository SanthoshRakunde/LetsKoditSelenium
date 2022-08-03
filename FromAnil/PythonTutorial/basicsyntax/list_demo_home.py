"""
Data type to store more than one value in one variable name
List items are in brackets, separated with "," [ 1, 2, 3 ]
"""

# cars = ["bmw", "audi", "honda"]
# print(cars)
# print(cars[1])
#
# empty_list = []
# print(empty_list)
# print("*#" * 20)
#
# cars[2] = "Benz"
# print(cars)
# print(cars[2])
# print("*#" * 20)
#
# num_list = [10, 20, 30]
# sum_num = num_list[0] + num_list[1]
#
# print(sum_num)
# print("*#" * 20)

cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)
print("*#" * 20)

cars.append("mustang")
print(cars)
print("*#" * 20)

cars.insert(1, "benz")
print(cars)
print("*#" * 20)

index = cars.index("benz")
print(index)
print("*#" * 20)

print(cars)
item = cars.pop()
print(item)
print(cars)
print("*#" * 20)

cars.remove("audi")
print(cars)
print("*#" * 20)

cars.append("audi")
cars.append("mustang")
print(cars)
print("*#" * 20)

sub1 = cars[0:3]
print(sub1)
sub2 = cars[:3]
print(sub2)
sub3 = cars[3:]
print(sub3)
print("*#" * 20)

print(cars)
cars.sort()
print(cars)