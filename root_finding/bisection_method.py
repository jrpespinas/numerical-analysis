# Copyright 2020 Jan Rodolf Espinas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Bisection Method using Python"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import numpy as np


__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'


TOL = 1e-6


def f(x):
    """
    A function that evaluates `x`.

    Parameters
    ----------
    x : int or float
        Any value to be evaluated

    Returns
    -------
    float
        the output of the function

    """
    # return -10 + x * (0 + x * (4 + x))
    # return (-6 + x * (14 + x * (-7 + x)))  # homework 1
    # return -2 + x * (3 + x * (-1 + (np.exp(x)))) # homework 2
    return np.log(x) + 4 + x * (-4 + x)  # homework 3


def check_root(a, b):
    """
    Verify if the root exist by checking the signs of `a` and `b`.

    Parameters
    ----------
    a : int or float
        Left endpoint
    b : int or float
        Right endpoint

    Return
    ------
    bool:
        Returns True if a root exist

    """
    if f(a) * f(b) < 0:
        return True


def bisection_method(a, b):
    """
    A root-finding algorithm which uses an iterative method
    similar to binary search.

    Parameters
    ----------
    a : int or float
        left endpoint
    b : int or float
        right endpoint

    """
    if check_root(a, b):
        i = 0
        while (b - a) / 2 > TOL:
            c = (a + b) / 2

            # Check if root found or tolerance exceeded
            if f(c) == 0:
                break

            # Reassign endpoints
            if f(c) * f(a) < 0:
                b = c
            else:
                a = c

            # Tolerance
            tol = (b - a) / 2

            # Display result
            if len(sys.argv) > 1:
                print(
                    f'{i+1}:\ta={a:.6f},\tb={b:.6f},\tc={c:.6f},'
                    f'\troot={f(c):.6f}\ttolerance={tol:.6f}'
                )
            else:
                print(f'{i+1}:\t root = {c:.7f},\ttolerance = {tol:.7f}')

            i += 1
    else:
        print("Root does not exist")


if __name__ == '__main__':
    # homework 1
    #bisection_method(0, 1)
    #bisection_method(1, 3.2)
    #bisection_method(3.2, 4)

    # homework 2
    #bisection_method(0, 1)

    # homework 3
    bisection_method(1, 2)
    bisection_method(2, 4)
