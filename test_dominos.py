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

def test_board_parser():
	assert ((6,), (1,)) == tuple(board_parser("6,1"))
	assert ((6,), (1,-1)) == tuple(board_parser("6,1_"))
	assert ((6,), (1,1)) == tuple(board_parser("6,11"))

def test_pair_dominos():
	assert (((6,1),(6,)),) == tuple(pair_dominos(((6,1),),((6,),)))
	assert (((6,1),(6,)),) == tuple(pair_dominos(((1,6),),((6,),)))
	assert (((6,1),(6,6)),) == tuple(pair_dominos(((6,1),),((6,6),)))
	assert (((6,1),(6,-1)),) == tuple(pair_dominos(((6,1),),((6,-1),)))
	assert (((6,1),(6,)),((1,6),(1,))) == tuple(pair_dominos(((6,1),),((6,),(1,))))
	assert (((6,1),(6,)),((1,6),(1,))) == tuple(pair_dominos(((6,1),(2,4)),((6,),(1,))))
	assert tuple() == tuple(pair_dominos(((6,1),),()))

def test_score_board():
	assert 1 == score_board([(1,)])
	assert 9 == score_board([(1,),(3,),(5,)])
	assert 6 == score_board([(3,3)])
	assert 0 == score_board([(3,-1)])

def test_score_pairs():
	assert (-5,)  == score_pairs([((6,1),(6,))])
	assert (5,)  == score_pairs([((1,6),(1,))])
	assert (5,1)  == score_pairs([((1,6),(1,)), ((3,4),(3,))])
	assert (6,)  == score_pairs([((1,6),(1,-1))])
	assert (4,)  == score_pairs([((1,6),(1,1))])
