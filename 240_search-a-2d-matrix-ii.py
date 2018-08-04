# -*- coding: utf-8 -*-
'''
---------------------------------------
@Time    : 2018/8/2 12:53
@Author  : Andy Zang
@File    : 240_search-a-2d-matrix-ii
@Software: PyCharm
@For     : 
---------------------------------------
'''


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for row in matrix:
        for each in row:
            if each == target:
                return True
    return False

if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(searchMatrix(matrix,target))
