#!usr/bin/env python
# -*- coding: utf-8 -*-
"""W5 - Task 03."""

def celsius_to_fahrenheit(temperature):
    return (9.0 * temperature) / 5 + 32

def fahrenheit_to_celsius(temperature):
    return (5 * (temperature - 32)) / 9.0

def convert_temperature(temperature, output_format='c'):
    temp = temperature
    given_input = None
    input_format = 'f'
    try:
        float(temperature)
    except ValueError:
        given_input = 'f' if temperature.endswith('f') else 'c'
        try:
            temp = float(temperature[:-1])
        except ValueError:
            return None
    if given_input is not None:
        input_format = given_input
    else:
        input_format = 'c' if output_format.lower() == 'f' else 'f'
    if input_format == 'f' and output_format == 'f':
        return temp
    elif input_format == 'c' and output_format == 'c':
        return temp
    elif input_format == 'f' and output_format == 'c':
        return fahrenheit_to_celsius(temp)
    elif input_format == 'c' and output_format == 'f':
        return celsius_to_fahrenheit(temp)
    return None


