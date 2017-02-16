class Furniture:
    def __init__(self):
        self.size = 0

class Chair(Furniture):
    def __init__(self):
        super().__init__()
        self.size = 1

class Table(Furniture):
    def __init__(self):
        super().__init__()
        self.size = 4

def new_Furniture():
    'factory'
    want = input("select type of new furniture")
    if want == 'ch':
        return Chair()
    elif want == 'tb':
        return Table()
    else:
        print("can't do it")
        return None

res = []
while True:
    obj = new_Furniture()
    if obj is None:
        print('bye')
        break
    res.append(obj)
print("Apartments", res)