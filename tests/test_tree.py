from segtree import SegmentTree

def test_tree_build():
    a = [1,2,3,4,5,6]
    t = SegmentTree(a)
    assert t.sum(1) == 21
    assert t.sum(2) == 6
    assert t.sum(3) == 15
    assert t.sum(4) == 3

    