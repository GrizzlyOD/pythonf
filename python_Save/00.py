import  operator
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Name': 'Mahnaz', 'Age': 27}
dict3 = {'Name': 'Abid', 'Age': 27}
dict4 = {'Name': 'Zara', 'Age': 7}

#py3 have no cmp (dict1, dict2)

print(operator.eq(dict1,dict2))
print(operator.eq(dict1,dict4))
