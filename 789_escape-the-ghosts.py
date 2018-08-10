# -*- coding: utf-8 -*-
'''
---------------------------------------
@Time    : 2018/8/8 22:40
@Author  : Andy Zang
@File    : 789_escape-the-ghosts
@Software: PyCharm
@For     : 
---------------------------------------
'''
import time


class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        dis = distence([0,0],target)
        for ghost in ghosts:
            if distence(ghost,target) <= dis:
                return False
        return True

def distence(start,target):
    return  abs(start[0]-target[0])+abs(start[1]-target[1])



if __name__ == '__main__':
    start = time.clock()
    ghosts = [[1, 0]]
    target = [2, 0]
    test = Solution
    print(test.escapeGhosts(test,ghosts,target))


    end = time.clock()
    print('Running time: %s Seconds' % (end - start))
    