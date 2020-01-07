
## Parses hand string into list of domino tuples
#  @param hand_str The string to prase
#  @return A list of tuples representing dominos
def hand_parser(hand_str):
	return [tuple([int(domino_num) for domino_num in domino_str.split("/")])
			for domino_str in hand_str.split(",")]

## Reverses a tuple
#  @param tup Changes the tuples
#  @return The tuple reversed
def reverse_tuple(tup):
	return tuple(reversed(tup))

## Filters out all dominos in list that do not include num
#  @param dominos List to filter down
#  @param num Number that needs to be in every domino
#  @return Filtered list containing only dominos with num
def filter_dominos(dominos, num):
	return tuple(filter(lambda x: num in x, dominos))

## Parses the board string into domino tuples
#
#  Each single domino is a tuple of one element.
#  Each double domino is a 2 element tuple with
#  either the original element or original and -1.
#  This depends if the double has been played on.
#  
#  @param board_str to parse
#  @return a list of dominos
def board_parser(board_str):
	def _item_parse(item):
		num = int(item[0])
		if len(item) == 1:
			return (num,)
		elif item[1] == "_":
			return (num, -1)
		else:
			return (num,num)
			
	return tuple([_item_parse(item.strip()) for item in board_str.split(",")])

## Pairs dominos in hand to board
#
#  Calculates all pairs of hand and board that match
#  @param hand The hand to pair with
#  @param board The board to pair against
#  @return A list of pairs
def pair_dominos(hand, board):
	hand += tuple([reverse_tuple(domino) for domino in hand])
	pairs = []
	for domino in hand:
		filtered = filter_dominos(board, domino[0])
		if filtered:
			pairs += [(domino,move) for move in filtered]

	return pairs

## Totals the score on the board
#
#  @param board Board to score
#  @return The boards current total
def score_board(board):
	def _score_domino(domino):
		num = domino[0]
		if len(domino) == 1:
			return num
		elif domino[1] == -1:
			return 0
		else:
			return num * 2

	return sum([_score_domino(domino) for domino in board])

