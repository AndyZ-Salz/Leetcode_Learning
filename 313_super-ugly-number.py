# -*- coding: utf-8 -*-
'''
---------------------------------------
@Time    : 2018/8/6 18:16
@Author  : Andy Zang
@File    : 313_super-ugly-number
@Software: PyCharm
@For     : 
---------------------------------------
'''
import time


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nn = 1 #"1" is the first one
        i = 1
        # ugly = primes
        while nn < n:
            i += 1
            if isUgly(i,primes):
                nn += 1
            # if isUglywithUgly(i,primes,ugly):
            #     nn += 1
        # print(ugly)
        return i

def isUgly(num,primes):
    if num in primes:
        return True
    for i in primes:
        if num % i == 0 and isUgly(num//i,primes):
            return True
    return False


def isUglywithUgly(num,primes,ugly):
    if num in ugly:
        # print(num," in ugly")
        return True
    for i in primes:
        if num % i == 0 and isUglywithUgly(num//i,primes,ugly):
            ugly.append(num)
            # print(num," calutale")
            return True
    return False


if __name__ == '__main__':
    start = time.clock()
    test = Solution
    # primes = [2, 7, 13, 19]
    # print(test.nthSuperUglyNumber(test,12,primes))
    print(test.nthSuperUglyNumber(test,800,
    [37, 43, 59, 61, 67, 71, 79, 83, 89, 97, 101, 103, 113, 127, 131, 157, 163, 167, 173, 179, 191, 193, 197, 199, 211,
     229, 233, 239, 251, 257]))
    end = time.clock()
    print('Running time: %f Seconds' % (end - start))

