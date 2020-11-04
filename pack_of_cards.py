import random

spades = ['A of spades', '2 of spades', '3 of spades', '4 of spades', '5 of spades', '6 of spades',
          '7 of spades', '8 of spades', '9 of spades', '10 of spades', 'J of spades', 'Q of spades', 'K of spades']
clubs = ['A of clubs', '2 of clubs', '3 of clubs', '4 of clubs', '5 of clubs', '6 of clubs',
         '7 of clubs', '8 of clubs', '9 of clubs', '10 of clubs', 'J of clubs', 'Q of clubs', 'K of clubs']
hearts = ['A of hearts', '2 of hearts', '3 of hearts', '4 of hearts', '5 of hearts', '6 of hearts',
          '7 of hearts', '8 of hearts', '9 of hearts', '10 of hearts', 'J of hearts', 'Q of hearts', 'K of hearts']
diamonds = ['A of diamonds', '2 of diamonds', '3 of diamonds', '4 of diamonds', '5 of diamonds', '6 of diamonds',
            '7 of diamonds', '8 of diamonds', '9 of diamonds', '10 of diamonds', 'J of diamonds',
            'Q of diamonds', 'K of diamonds']

pack_of_cards = spades + clubs + hearts + diamonds
count = 0

while count < 52:
    rand_card = random.choice(pack_of_cards)
    print(str(count + 1) + ' - ' + rand_card)
    pack_of_cards.remove(rand_card)
    count += 1
