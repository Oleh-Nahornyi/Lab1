class Dude():
    def __init__(self, name):
        self._name = name

class Do():
    def __init__(self, dude):
        self._dude = dude

    def say(self):
        print('{}, say hello'.format(self._dude._name))


dude = Dude("Jorick")



dude_do = Do(dude)
dude_do.say()
