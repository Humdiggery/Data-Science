# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 07:08:20 2016

@author: Katie
"""
def side_effect_test(value):
    # Do something to modify the value
    value[1] = "orange"
    print("Inside the function, the value becomes {}".format(value))

if __name__ == "__main__":
    # Create the value
    value = 0

    print("Outside the function, the value starts as {}".format(value))

    side_effect_test(value)

    print("Outside the function, the value is now {}".format(value))