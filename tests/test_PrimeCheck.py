#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.PrimeCheck import PrimeCheck

import pytest


class TestPrimeCheck(object):

    @pytest.mark.parametrize("num", [5, 7, 11])
    def test_is_prime_true(self, num):
        pc = PrimeCheck()
        assert pc.is_prime(num)

    @pytest.mark.parametrize("num", [4, 6, 8])
    def test_is_prime_false(self, num):
        pc = PrimeCheck()
        assert pc.is_prime(num) == False