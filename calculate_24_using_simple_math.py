# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14th, 2019

This is the solution to calculating 24 based on sequence of numbers provided, and
    it will only use +, -, *, / operations

It needs Python 3

@author: Man
"""


def equivalent(a, b):
    if abs(a-b) < 1e-8:
        return True
    else:
        return False


def solution(q, a, cache={}):
    a = round(a, 10)
    if len(q) <=1:
        if q[0] == a:
            cache[(q,a)] = str(a)
        else:
            cache[(q,a)] = None
        return cache[(q, a)]
    elif len(q)==2:
        m1,m2 = q[0], q[1]
        if equivalent(m1+m2, a):
            cache[(q,a)] = "("+str(m2)+ "+"+ str(m1)+")"
        elif equivalent(m2-m1, a):
            cache[(q,a)] = "("+str(m2)+ "-"+ str(m1)+")"
        elif equivalent(m1-m2, a):
            cache[(q,a)] = "("+str(m1)+ "-"+ str(m2)+")"
        elif equivalent(m2/m1, a):
            cache[(q,a)] = "("+str(m2)+ "/"+ str(m1)+")"
        elif equivalent(m1/m2, a):
            cache[(q,a)] = "("+str(m1)+ "/"+ str(m2)+")"
        elif equivalent(m2*m1, a):
            cache[(q,a)] = "("+str(m2)+ "*"+ str(m1)+")"
        else:
            cache[(q,a)] = None
        return cache[(q, a)]
    else:
        for i, v in enumerate(q):
            q_ = tuple(list(q[:i]) + list(q[i+1:]))
            if cache.get((q, a)) is None:
                if (q_, a-v) not in cache:
                    cache[(q_, a-v)] = solution(q_, a-v, cache=cache)
                if cache.get((q_, a-v)) is not None:
                    cache[(q, a)] = "(" + cache[(q_, a-v)] + "+" + str(v)+ ")"
            if cache.get((q, a)) is None:
                if (q_, v-a) not in cache:
                    cache[(q_, v-a)] = solution(q_, v-a, cache=cache)
                if cache.get((q_, v-a)) is not None:
                    cache[(q, a)] = "(" + str(v) + "-" + cache[(q_, v-a)] + ")"
            if cache.get((q, a)) is None:
                if (q_, a*v) not in cache:
                    cache[(q_, a*v)] = solution(q_, a*v, cache=cache)
                if cache.get((q_, a*v)) is not None:
                    cache[(q, a)] = "(" + cache[(q_, a*v)] + " / " + str(v) + ")"
            if cache.get((q, a)) is None:
                if (q_, a+v) not in cache:
                    cache[(q_, a+v)] = solution(q_, a+v, cache=cache)
                if cache.get((q_, a+v)) is not None:
                    cache[(q, a)] = "(" + cache[(q_, a+v)] + " - " + str(v) + ")"
            if cache.get((q, a)) is None:
                if (q_, a/v) not in cache:
                    cache[(q_, a/v)] = solution(q_, a/v, cache=cache)
                if cache.get((q_, a/v)) is not None:
                    cache[(q, a)] = "(" + cache[(q_, a/v)] + " * " + str(v) + ")"
            if cache.get((q, a)) is None:
                if (q_, v/a) not in cache:
                    cache[(q_, v/a)] = solution(q_, v/a, cache=cache)
                if cache.get((q_, v/a)) is not None:
                    cache[(q, a)] = "(" + str(v) + "/" + cache[(q_, v/a)] + ")"
            if cache.get((q, a)):
                return cache[(q, a)]



solution(q=(1,5,5,5), a=24)
solution(q=(2,2,13,13), a=24)
