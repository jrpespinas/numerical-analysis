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

"""Evaluating Polynomials using Horner's Method in Python"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'


def evaluate(x, degree, coefficients, base):
    pass


def f(x):
    return (x ** 3) + (4 * (x ** 2)) - 10


if __name__ == "__main__":
    print(evaluate(3, 4, [1, 4, 0, -10], [0, 0, 0, 0]))
    print(f(3))
