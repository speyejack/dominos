from dominos import *


def test_hand_parser():
	assert ((1,2),(3,4),(5,6)) ==  tuple(hand_parser("1/2,3/4,5/6"))
	assert ((6,4),) ==  tuple(hand_parser("6/4"))

def test_reverse_tuple():
	assert (1,2) == reverse_tuple((2,1))
	assert (6,1) == reverse_tuple((1,6))

def test_filter_dominos():
	assert () == tuple(filter_dominos([(1,2),(3,4),(5,6)],0))
	assert ((1,2),) == tuple(filter_dominos([(1,2),(3,4),(5,6)],1))
	assert ((5,6),) == tuple(filter_dominos([(1,2),(3,4),(5,6)],6))
	assert ((1,2),(2,4)) == tuple(filter_dominos([(1,2),(2,4),(5,6)],2))
