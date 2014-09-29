#!usr/bin/env python
# -*- coding: utf-8 -*-
"""W5 - Task 01."""

def bool_to_str(bvalue, short=False):
    if bvalue and not short:
        return 'Yes'
    elif bvalue and short is True:
        return 'Y'
    elif not short:
        return 'No'
    return 'N'

