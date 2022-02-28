from segtree import SegmentTree


def test_tree_sum():
    a = [1, 2, 3, 4, 5, 6]
    t = SegmentTree(a)
    assert t.sum(0,2) == 6
    assert t.sum(0,3) == 10
    assert t.sum(3,5) == 15
    assert t.sum(0,12) == 21

def test_empty_tree():
    a = []
    t = SegmentTree(a)
    assert t.sum(0,0) == 0
    assert t.sum(-1,0) == 0
    assert t.sum(0,12) == 0
    
def test_overlap():
    t = SegmentTree([])
    assert not t._overlap(0, 3, 4, 6)
    assert t._overlap(0, 3, 3, 6)
    assert t._overlap(0, 3, 2, 6)
    assert t._overlap(1, 3, 0, 6)
    
    assert not t._overlap(4, 6, 0, 3)
    assert t._overlap(3, 6, 0, 3)
    assert t._overlap(2, 6, 0, 3)
    assert t._overlap(0, 6, 1, 3)