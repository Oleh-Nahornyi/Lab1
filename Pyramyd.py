

class Pyramid:
    def rigth(self, card_numb, row):
        return card_numb + 1 - row

    def left(self, card_numb, row):
        return card_numb - row

    def call(self, card_numb):

        sum = 0
        row = 0
        while sum < card_numb:
            sum += row + 1
            row += 1
        print(sum)
        if card_numb == sum:
            print('This is right edge card')
            return [self.left(card_numb, row)]
        elif card_numb == sum + 1 - row:
            print('This is left edge card')
            return [self.rigth(card_numb, row)]
        else:
            print('This is middle card')
            return [self.left(card_numb, row), self.rigth(card_numb, row)]

    def add(self, card: Card):

