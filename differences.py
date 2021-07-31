# DIFFERENCE BETWEEN
# LIST - square braces
# TUPLE - rounded braces
# SET - the set keyword
# DICTIONARY - curly braces: made up of key-value pairs

list1 = ["anggur", "ayam", "pisang", 92, 42]
list1[0] = "baru"  # list boleh berubah
y = list(list1)
y[1] = "Replaced"
thisArray = tuple(y)
print(list1)
print(thisArray)

tuple1 = ("anggur", "ayam", "pisang", 92, 42)
# tuple1[0] = "baru"  # tuple tak boleh berubah
print(tuple1)

set0 = set(["set", "ayam", "pisang", 92, 42])
set1 = {"set", "pisang", "pisang", 92, 42}  # set aren't repeatable(pisang)
# Note: the set list is unordered,
# meaning: the items will appear in a random order.
# Once a set is created, you cannot change its items,
# but you can add new items.
print(set1)
print(len(set1))

dict1 = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print(dict1)
