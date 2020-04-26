### Ngui Jia Xuan, Sheriann 1004641
### 10.009 The Digital World Final Assignment

from libdw import sm
import random
import time
import sys

# Mapping out the gameboard (reference attached in zip file)
maxisquare = 100

# key: square players land on; value: square player goes to
snakes = {32: 10, 
		36: 6,
		48: 26,
		62: 18,
		88: 24,
		95: 56,
		97: 78}

ladders = {1: 38,
		4: 14,
		8: 10,
		21: 42,
		28: 76,
		50: 67,
		71: 92,
		88: 99}

class Player:
	def __init__(self, name = '', square = 0):
		self.name = name
		self.square = square 

# Introduction to game
def intro():
	print('HiHI hELLo its my DW game: Snakes n Ladders!')
	P1.name = input('Player 1! what is your name?: ')
	time.sleep(1)
	print('COOL')
	P2.name = input('And you, Player 2?: ')
	time.sleep(1)
	print('COOL TOO')
	print('\n')
	print('''Ok, here are the rules:
	1. Both of u start at 0, roll the dice to rise the ranks.
	2. Beware of ssslipery sssnakes along the way!
	3. Ladders will help you up :)
	4. First to 100 wins mwahahaha''')
	time.sleep(1)
	print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n*ding ding ding* May the cooler human win!!!')

	return P1, P2 

# To check if player has met the win condition 
def check_win(player):
	time.sleep(1)
	if player.square >= maxisquare: 
		print("{} wins!! You're the cooler human!!!!".format(player.name))
		time.sleep(1)
		print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \nWeehu!! Thanks for playing my game! Hope you enjoyed it :)')
		sys.exit(1)
	else:
		return False

def roll_dice():
	time.sleep(1)
	value = random.randint(1, 6)
	print('You rolled {}!'.format(value))

	return value 

# Str variations to make game more entertaining
snake_texts = ['O boy.. Got some bad news for you', 'OOPSIES u hit a badsies', 'HOORA--oh \nohhhh no', 'um.. how do I tell this to you...', '......heh a snake', 'AAAAAAAA SNAKE', "WOOP WOOP YOU GOT A SNAKE!! {}\nwaaait that isn't good?".format(time.sleep(1)), 'bummer..']
ladder_texts = ['YIPPEEE YOU GOT A GOODIEEE!', 'SHOOORTTCUUUTTTT', 'YAY a ladder', 'nailed it.']
next_turn = ['your turn! ', "let's win this! ", 'ya ready? ', 'GOOOO!! ', 'you got this ;) ', "you're up! ", '']

def snake_bite(player, new_square):
	print('\n' + random.choice(snake_texts))
	time.sleep(1)
	print('\n{} got a snake bite. Down from {} to {}.'.format(player.name, str(player.square), str(new_square)))

	return new_square

def ladder_jump(player, new_square):
	print('\n' + random.choice(ladder_texts))
	time.sleep(1)
	print('\n{} climbed the ladder. Up from {} to {}.'.format(player.name, str(player.square), str(new_square)))

	return new_square


class GamePlay(sm.SM):
	start_state = 'P1_turn'

	def get_next_values(self, state, inp):

		if self.state == 'P1_turn':
			value = roll_dice()
			time.sleep(1)
			print('You moved from {} to {}.'.format(str(P1.square), str(P1.square + value)))
			P1.square += value 

			# check if player landed on a snake or ladder
			if P1.square in snakes:
				P1.square = snake_bite(P1, snakes[P1.square])

			elif P1.square in ladders:
				P1.square = ladder_jump(P1, ladders[P1.square])

			return 'P2_turn', P1

		if self.state == 'P2_turn':
			value = roll_dice()
			time.sleep(1)
			print('You moved from {} to {}.'.format(str(P2.square), str(P2.square + value)))
			P2.square += value 

			# check if player landed on snake or ladder
			if P2.square in snakes:
				P2.square = snake_bite(P2, snakes[P2.square])

			elif P2.square in ladders:
				P2.square = ladder_jump(P2, ladders[P2.square])

			return 'P1_turn', P2

# instantiating as global variable since made used of in all functions
P1 = Player()
P2 = Player()
def SnakesnLadders():
	intro()

	game = GamePlay()
	game.start()

	# keeps switching between players' turn as long as win condition not met
	while True:
		# player 1's turn
		game.step(input("\n{}, ".format(P1.name) + random.choice(next_turn) + "'Enter' to the roll dice:"))
		# checking win condition
		check_win(P1)

		# player 2's turn
		game.step(input("\n{}, ".format(P2.name) + random.choice(next_turn) + "'Enter' to the roll dice:"))
		# checking win condition
		check_win(P2)


if __name__ == '__main__':
	SnakesnLadders()
