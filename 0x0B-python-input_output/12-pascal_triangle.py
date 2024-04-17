#!/usr/bin/python3
"""
    def pascal_triangle().
"""


def pascal_triangle(n):
    """
        returns a lis of lists of ints.
        Args:
            n (int): numb of lsts and digits.
        Returns: lst of lsts.
    """
    t_row = [1]
    temp_l = [0]
    pTri = []

    if n <= 0:
        return pTri

    for i in range(n):
        pTri.append(t_row)
        t_row = [l+r for l, r in zip(t_row + temp_l, temp_l + t_row)]
    return pTri
