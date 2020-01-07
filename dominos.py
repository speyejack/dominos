
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

## Calculates the score of each pair
#
#  @param pairs Tuples of pairs to score
#  @return A tuple of pairs and scores
def score_pairs(pairs):
	def _score_pair(pair):
		domino,match = pair
		if len(match) == 1:
			return domino[1] - domino[0]
		elif match[1] == -1:
			return domino[1]
		else:
			return domino[1] - domino[0] * 2

	return tuple(_score_pair(pair) for pair in pairs)
		
## Calculates total score for the board and pairs
#
#  @param pairs Tuples of pairs to score
#  @param board Board to score
#  @return A tuples of pair and score
def total_score(pairs,board):
	board_score = score_board(board)
	scores = [pair_score + board_score for pair_score in score_pairs(pairs)]
	return tuple((dom[0],dom[1],scores[i]) for i,dom in enumerate(pairs))

## Creates a string representation of the pairs
#
#  @param pairs Tuples of scored pairs to convert to string
#  @return A string representation of the pairs
def pair_to_string(pairs):
	def _create_str(pair):
		domino,match,score = pair
		if len(match) == 1:
			string = "{}/{} -> {} = {}".format(domino[0], domino[1], match[0], score)
		elif match[1] == -1:
			string = "{}/{} -> {}_ = {}".format(domino[0], domino[1], match[0], score)
		else:
			string = "{}/{} -> {} = {}".format(domino[0], domino[1], match, score)
		return string
	return "\n".join([_create_str(pair) for pair in pairs])

## Converts a string of a hand and board into a scored pairing
#
#  @param hand_str String representation of a hand
#  @param board_str String representation of the board
#  @return A string representation of all solved pairs
def solve_dominos(hand_str, board_str):
	hand = hand_parser(hand_str)
	board = board_parser(board_str)

	pairs = pair_dominos(hand, board)

	score = total_score(pairs,board)

	pair_string = pair_to_string(score)
	return pair_string
