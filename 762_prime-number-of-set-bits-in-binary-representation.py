# -*- coding: utf-8 -*-
'''
---------------------------------------
@Time    : 2018/8/4 11:02
@Author  : Andy Zang
@File    : 762_prime-number-of-set-bits-in-binary-representation
@Software: PyCharm
@For     : 
---------------------------------------
'''


def countPrimeSetBits(L, R):
    """
    :type L: int
    :type R: int
    :rtype: int
    """
    count = 0
    for each in range(L, R + 1):
        if primeNumber(numberOfOne(each)):
            count += 1
    return count


def numberOfOne(raw):  # bin(raw).count('1')
    one = 0
    while raw != 0:
        if raw % 2 == 1:
            one += 1
        raw = raw // 2
    return one


def primeNumber(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(countPrimeSetBits(990, 1048))
