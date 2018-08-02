# -*- coding: utf-8 -*-
'''
---------------------------------------
@Time    : 2018/8/2 9:23
@Author  : Andy Zang
@File    : 856_score-of-parentheses
@Software: PyCharm
@For     : 
---------------------------------------
'''

def main (S):
    """
        :type S: str
        :rtype: int
    """
    level = -1
    mid = []
    score = 0
    for each in S:
        if each == '(':
            level = level + 1
        else:
            if last == '(':
                mid.append(level)
            level = level - 1
        last = each


    for eachlevel in mid:
        score = score + 2 ** eachlevel

    return score


if __name__ == '__main__':
    print(main("(()(()))"))
