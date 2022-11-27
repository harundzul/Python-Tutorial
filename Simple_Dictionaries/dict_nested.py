"""

- Dictionaries in python is used to stored data value in pairs
- It is written with curly brackets, have keys, and value
    - Eg for Key and Value in this code:
    - Key = "name"
    - Value = "Emil"
- Dictionary is changeable and not allow to duplicate

- In this case, "child1-3" hold both the key and value of a specific item
- meanwhile, "myfamily" hold the overall key and value of "child1-3"

"""

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"])