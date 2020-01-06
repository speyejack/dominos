
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

