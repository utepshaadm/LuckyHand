''' Lucky Hand Cipher'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class LH:
    def __init__(self):
        self.deck = list(range(52))
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.suits = []
        c = 0
        for x in range(4):
        	for y in range(13):
        		self.suits.append(c)
        	c += 13
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def get_val(self, x):
         return self.values[x]
         
    def ksa(self):
        self.deck.append(self.deck.pop(0))
        self.deck.append(self.deck.pop(0))

        card1 = self.get_val(self.deck[0]) - 1
        card1_suit = self.suits[self.deck[0]]

        card2 = self.get_val(self.deck[1]) - 1
        card2_suit = self.suits[self.deck[1]]
        total = card1 + card2
        if card1_suit == card2_suit:
        	total = total * 2
        self.deck.append(self.deck.pop(total))
        for x in range(total):
        	self.deck.append(self.deck.pop(3))
        v = self.get_val(self.deck[0])
        z = self.get_val(self.deck[v])
        return self.deck[v + z] % 26
         
    def encrypt_letter(self, letter):
        key = self.ksa()
        num = ord(letter) - 65
        num = (num + key) % 26
        return chr(num + 65)
        
    def decrypt_letter(self, letter):
        key = self.ksa()
        num = ord(letter) - 65
        num = (num - key)
        return chr(num + 65)

    def encrypt(self, letters):
        ctxt = []
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters):
        ptxt = []
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)
