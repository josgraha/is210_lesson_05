#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal
import math

def main():
    pstr = raw_input('what is the amount of your principal?: ')
    dstr = raw_input('for how many years is this loan being borrowed?: ')
    qstr = raw_input('are you prequalified for this loan?: ')

    # function arguments should not need the following three transformations
    # delete these lines when function conversion is complete
#    principal = int(pstr)
#    duration = int(dstr)
#    prequalification = true if qstr.lower()[0] == 'y' else false
    pq = True if qstr.lower()[0] == 'y' else False
    # function conversion work you do should start here
    interval = 12
    total = calculate_total(pstr, dstr, pq)




def get_interest_rate(principal=0.0, duration=0.0, prequalification=False):
    rate = None
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0363'
            else:
                rate = '0.0465'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0404'
            else:
                rate = '0.0498'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0577'
            else:
                rate = '0.0639'
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0302'
            else:
                rate = '0.0398'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0327'
            else:
                rate = '0.0408'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0466'
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0205'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0262'
    if rate is None:
        return None
    rate = decimal.Decimal(rate)
    return rate

def compound_interest(principal=0.0, duration=0.0, rate=None, interval=12):
    if rate is None:
        return None
    total = principal * ((1 + rate / interval) ** (interval * duration))
    if total is None:
        return None
    return total

def calculate_total(principal=0.0, duration=0.0, prequalification=False, interval=12):
    principal = int(principal)
    duration = int(duration)
    rate = get_interest_rate(principal, duration, prequalification)
    if rate is None:
        return None
    total = compound_interest(principal, duration, rate)
    return int(total)

def calculate_interest(principal=0.0, duration=0.0, prequalification=False, interval=12):
    rate = get_interest_rate(principal, duration, prequalification)
    if rate is None:
        return None
    total = compound_interest(principal, duration, rate)
    if total is None:
        return None
    interest = total - principal
    interest = int(math.ceil(interest))
    return interest