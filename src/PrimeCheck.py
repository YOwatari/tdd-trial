#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PrimeCheck(object):

    def is_prime(self, num):
        result = True
        for i in range(2, num):
            if num % i == 0:
                result = False
                break

        return result
