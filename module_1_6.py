my_dict = {'Marina': 1985, 'Alex': 2008,'Ilya': 2014}
print('Dict:',my_dict)
print('Existing value:',my_dict['Marina'])
print('Not existing value:', my_dict.get('Kolya'))
a = my_dict.pop('Alex')
print('Deleted value:',a)
my_set = {1,2,3,'A','B',1,2,5, (5,6,7), 'one'}
print ("Set:", my_set)
my_set.update([6,7])
my_set.remove(2)
print('Modified set:',my_set)