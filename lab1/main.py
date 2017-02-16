from singletone import a
print(a)


def singleton(cls):
    "It prevents the creation of an object more than once"
    instances = {}
    def getinstance():
        print("inst", instances)
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class myClass:
    "mockup for singletone test"
    pass

@singleton
class myClass1:
    "mockup for singletone test"
    pass

obj1 = myClass()
obj2 = myClass()
print(obj1 is obj2)

obj1 = myClass1()
obj2 = myClass1()
print(obj1 is obj2)
