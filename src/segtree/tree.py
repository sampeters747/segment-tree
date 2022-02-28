from typing import List, Optional


class SegmentTree:

    def __init__(self, array: List[int]) -> None:
        n = len(array)
        self.tree_l = 0
        self.tree_r = n-1
        self._tree: List[int] = [0 for i in range(4 * n + 2)]
        if self.tree_r >= 0:
            self._build(array, 1, self.tree_l, self.tree_r)

    def sum(self,
            sum_lb: int, sum_rb: int, tree_index: int = 1,
            seg_lb: Optional[int] = None, seg_rb: Optional[int] = None) -> int:
        if seg_lb is None:
            seg_lb = self.tree_l
        if seg_rb is None:
            seg_rb = self.tree_r
        if sum_lb == seg_lb and sum_rb == seg_rb:
            return self._tree[tree_index]
        elif sum_lb <= seg_lb and sum_rb >= seg_rb:
            return self._tree[tree_index]
        else:
            left, right = 0, 0
            midpoint = self._midpoint(seg_lb, seg_rb)
            if self._overlap(sum_lb, sum_rb, seg_lb, midpoint):
                left = self.sum(sum_lb, sum_rb, self._lchild(tree_index), seg_lb=seg_lb, seg_rb=midpoint)
            if self._overlap(sum_lb, sum_rb, midpoint+1, seg_rb):
                right = self.sum(sum_lb, sum_rb, self._rchild(tree_index), seg_lb=midpoint+1, seg_rb=seg_rb)
            return left + right

    def _overlap(self, l1: int, r1: int, l2: int, r2: int):
        if r2 > r1:
            return l2 <= max(l1, r1)
        else:
            return l1 <= max(l2, r2)

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

    def _midpoint(self, lb: int, rb: int) -> int:
        return (lb + rb) // 2

    def _parent(self, i: int) -> int:
        return i // 2

    def _lchild(self, i: int) -> int:
        return 2 * i

    def _rchild(self, i: int) -> int:
        return 2 * i + 1
