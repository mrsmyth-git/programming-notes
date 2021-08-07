# Can contain multiple values but most of the time contain one value
list = ['anyvalue', 234, True]

print(list[2])

# Can contain multiple values
tuple = (234, 'hello', 234234)

print(tuple[1])

# Any data repeated in a set will not be saved
my_set = set()
set = {'one', 'value', 'at', 'at', 'a', 'a', 'time'}

print(set[0])

# In dictionaries data gets accessed by the keyword
dictionary = {'keyword': 'data', 
              'anotherkeyword': 'moredata'}

print(dictionary['keyword'])