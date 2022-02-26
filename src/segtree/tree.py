class SegmentTree:
    def __init__(self) -> None:
        pass

    def _parent(self, i: int) -> int:
        return (i-1)//2

    def _lchild(self, i: int) -> int:
        return 2*i+1

    def _rchild(self, i: int) -> int:
        return 2*i+2
