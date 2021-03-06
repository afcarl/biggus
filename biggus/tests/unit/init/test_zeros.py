# (C) British Crown Copyright 2014 - 2016, Met Office
#
# This file is part of Biggus.
#
# Biggus is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Biggus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Biggus. If not, see <http://www.gnu.org/licenses/>.
"""Unit tests for `biggus.zeros`."""

from __future__ import absolute_import, division, print_function
from six.moves import (filter, input, map, range, zip)  # noqa

import unittest

import numpy as np

from biggus import zeros
from biggus.tests import mock


class Test(unittest.TestCase):
    def test_dtype(self):
        dtype = 'i2'
        array = zeros((), dtype)
        self.assertIs(array.dtype, np.dtype(dtype))

    def test_dtype_default(self):
        array = zeros(())
        self.assertEqual(array.dtype, np.dtype('f8'))

    def test_shape(self):
        shape = (70, 768, 1024)
        array = zeros(shape)
        self.assertEqual(array.shape, shape)

    def test_value(self):
        array = zeros(())
        self.assertEqual(array.value, 0)


if __name__ == '__main__':
    unittest.main()
