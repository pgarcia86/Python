##  Sets. Los sets no admiten elementos duplicados. Se pueden unir dos sets, pero mediante el método union
##  Es desordenado, no puede hacerse subscripts de un set.

my_set = {}
my_other_set = {}
new_set = {}


my_set = {'Pablo', 'Garcia',37,1.66}
my_other_set = {'Sebastian', 'Pissinis', 41, 1.77}
print(my_set)
print(my_other_set)

my_set.add("Barros")
print(my_set)

my_set.clear()
print(my_set)

my_set = {'Pablo', 'Garcia', 'Barros',37,1.66}

new_set = my_set.union(my_other_set)
print(new_set)


my_set.remove('Pablo')
print(my_set)

my_set.add('Barros')

print(new_set.difference(my_set))
print(new_set.difference(my_other_set))