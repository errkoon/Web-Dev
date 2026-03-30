from models import Animal, Dog, Cat

a1 = Dog("Buddy", 3, "house", "golden")
a2 = Cat("Luna", 2, "flat", "black")
a3 = Animal("Animal", 5, "forest")

arr = [a1, a2, a3]

for i in arr:
    print(i)
    print(i.speak())
    print(i.move())

print(a1.fetch())
print(a2.climb())