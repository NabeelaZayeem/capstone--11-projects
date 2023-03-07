from collections import namedtuple
person=namedtuple('person',['name','age','gender'])
p=person('Alice',25,'female')
print(p.name)
print(p.age)
print(p.gender)