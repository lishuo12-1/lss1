import random

print(random.randint(1,10))
print(random.randrange(1,10))
list1=[1,2,3,4]
print(random.sample(list1,k=2))
print(random.choices(list1,k=2))
print(random.choice(list1))

random.shuffle(list1)
print(list1)

random.seed(10)
print(random.randint(1,10))
print()
random.seed(10)
