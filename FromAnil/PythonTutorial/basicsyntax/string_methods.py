"""
Examples to show available string methods in python
"""

# Accessing characters in a string
# index starts from zero
a = "nyc"
first = "nyc"[0]
print(first)
second = a[1]
print(second)
print("************************************")

"""
len()
lower()
upper()
str()
"""

string_example = "This is a Mixed case String"
lower_result = string_example.lower()
print(string_example)
print(lower_result)
print(string_example.lower())
print("************************************")

upper_result = string_example.upper()
print(string_example)
print(upper_result)
print("************************************")

size = len(string_example)
print(size)
print("************************************")

print(lower_result + " " + upper_result)
concat_result = lower_result + " " + upper_result
print(concat_result)

print("************************************")

# Replace Method
a = "1abc2xyz1abc2abc"
print(a.replace('abc', 'ABC'))

print("************************************")

# Sub-Strings
# starting index is inclusive
# Ending index is exclusive

sub = a[9:12]
print(sub)
step = a[2:12:2]
print(step)

print("************************************")

# Strings Formatting
city = "nyc"
event = "show"
example = "Welcome to {0} and enjoy the {1}"

print(example.format(city, event))