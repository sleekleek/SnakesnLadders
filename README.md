_Ngui Jia Xuan, Sheriann 1004641_
_10.009 The Digital World Final Assignment_

# Snakes n Ladders
The game is based off an existing classic board game: Snakes & Ladders. 
In fact, the virtual board in my code is based off an actual board (see below).

I also added informal but fun and uplifting commentary along the way to make the game more entertaining.

![Image][1]

## Prerequisiites
- Python 3 and above
    - `libdw 4.3.0`

## How to Play
Run the game in Python.

Players are prompted to input their name at the start.
They are then briefed on how to play the game (more informally in game):
1. Players start at square 0, rolling the dice to reach a higher square. 
2. Along the way, they may land on ladders or snakes.
3. Ladders provide a shortcut to a higher square;
4. Snakes bring you down to a lower square. 
5. The first player to reach 100 wins.

At the start of each turn, the player presses 'Enter' to roll the dice and the printed output on the screen constantly updates players on the game: what square he/she is at, whether he/she has landed on a ladder or a snake, etc.
This keeps track of their progress, and the moment one of them reaches the 100th square, the game declares a winner. 


## Description of Code
**Main functions and classes:**

**1) Player (class):**
By adding name and square as an attribute, returning an instance (from the functions) is much easier and neater.

```
class Player:
	def __init__(self, name = '', square = 0):
		self.name = name
		self.square = square 	# initialised at 0 since all players start at square 0
```

Instantiation also looks more elegant.

```
P1 = Player()
P2 = Player()
```


**2) SnakesnLadders (function):**
This is the backbone of the game. 

First, `intro()` welcomes the player to the game and briefs them on the game. Most importantly, it changes the players name (in the main frame) to the class Player mentioned above, for future references. 

Then, the state machine GamePlay (mentioned below) is instantiated with `game = GamePlay()` `game.start()`. 

Using the state machines, a `while` loop is run, switching between each players turn and checking if they have hit the 100th square, using functions `game.step()` and `check_win()` respectively. 
This `while` loop is key, keeping the game running as long as win condition is not met.

```
def SnakesnLadders():
	intro()

	game = GamePlay()
	game.start()

	# keeps switching between players' turn as long as win condition not met
	while True:
		game.step(input("\n{}, ".format(P1.name) + random.choice(next_turn) + "'Enter' to the roll dice:"))		# player 1's turn
		check_win(P1) 	# checking win condition

		game.step(input("\n{}, ".format(P2.name) + random.choice(next_turn) + "'Enter' to the roll dice:"))		# player 2's turn
		check_win(P2) 	# checking win condition
```


**3) GamePlay (subclass of sm.SM)**
This state machine has 2 states: `P1_turn` and `P2_turn`, making it easy to switch between turns. 

```
from libdw import sm

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
```


[1]: https://cdn.shopify.com/s/files/1/0876/1176/files/i984_pimgpsh_fullsize_distr.png?v=1525140332