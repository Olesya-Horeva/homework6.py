my_dict = {"Olesya": 1994,'Masha': 1993, 'Diana': 2005}
print(my_dict)
print(my_dict['Olesya'])
print(my_dict.get('Dasha'))
my_dict.update({'Dasha': 1998, 'Mira': 2023})
print(my_dict)
a = my_dict.pop('Olesya')
print(my_dict)
print(a)
my_set = {2,3,5,'Olesya',2,5,'Olesya'}
print(my_set)
print(my_set.add(1))
print(my_set.add('Masha'))
print(my_set.discard(2))
print(my_set)

