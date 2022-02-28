from typing import List, Optional


class SegmentTree:

    def __init__(self, array: List[int]) -> None:
        n = len(array)
        self.lb = 0
        self.rb = n-1
        self._tree: List[Optional[int]] = [0 for i in range(4 * n)]
        self._build(array, 1, self.lb, self.rb)
        
    def sum(self, l: int, r: int, ti: int = 1, lb: int = self.lb, rb: int = self.rb) -> int:
        if l == lb and r == rb:
            return self._tree[ti]
        elif  l <= lb and r >= rb:
            return self._tree[ti]
        else:
            left, right = 0, 0
            midpoint = self._midpoint(lb, rb)
            if self._overlap(l, r, lb, midpoint):
                left = self.sum(l, r, self._lchild(ti), lb=lb, rb=midpoint)
            if self._overlap(l, r, self._rchild(ti))


    def _overlap(l1: int, r1: int, l2: int, r2: int):
        return l1 <= l2 and r1 <= r2 or l2 <= l1 and r2 <= r1

    def _build(self, a: List[int], ti: int, lb: int, rb: int):
        segment_sum = 0
        for i in range(lb, rb + 1):
            segment_sum += a[i]
        self._tree[ti] = segment_sum
        if lb != rb:
            midpoint = self._midpoint(lb, rb)
            # left child
            self._build(a, self._lchild(ti), lb, midpoint)
            # right child
            self._build(a, self._rchild(ti), midpoint + 1, rb)

    def _midpoint(lb: int, rb: int) -> int:
        return (lb + rb) // 2

    def _parent(self, i: int) -> int:
        return i // 2


    def _lchild(self, i: int) -> int:
        return 2 * i


    def _rchild(self, i: int) -> int:
        return 2 * i + 1
