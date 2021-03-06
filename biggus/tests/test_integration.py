# (C) British Crown Copyright 2013 - 2016, Met Office
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
from __future__ import absolute_import, division, print_function
from six.moves import (filter, input, map, range, zip)  # noqa

import unittest

import numpy as np

import biggus
from biggus.tests import mock


class TestChaining(unittest.TestCase):
    def test_mean_of_difference(self):
        shape = (3, 4)
        size = np.prod(shape)
        raw_data1 = np.linspace(0.2, 1.0, num=size).reshape(shape)
        raw_data2 = np.linspace(0.3, 1.5, num=size).reshape(shape)
        array1 = biggus.NumpyArrayAdapter(raw_data1)
        array2 = biggus.NumpyArrayAdapter(raw_data2)
        difference = biggus.sub(array2, array1)
        mean_difference = biggus.mean(difference, axis=0)

        # Check the NumPy and biggus numeric values match.
        result = mean_difference.ndarray()
        numpy_result = np.mean(raw_data2 - raw_data1, axis=0)
        np.testing.assert_array_equal(result, numpy_result)

    def test_mean_of_mean(self):
        data = np.arange(24).reshape(3, 4, 2)
        array = biggus.NumpyArrayAdapter(data)
        mean1 = biggus.mean(array, axis=1)
        mean2 = biggus.mean(mean1, axis=-1)
        expected = np.mean(np.mean(data, axis=1), axis=-1)
        result = mean2.ndarray()
        np.testing.assert_array_equal(result, expected)

    def test_masked_array_numpy_first_biggus_second(self):
        # Ensure that an operation where the biggus array is second (i.e.
        # calling the special method of the numpy array not the biggus array,
        # returns the expected type).
        mask = [False, True, False]
        arr = np.ma.array([1, 2, 3], mask=mask)
        barr = biggus.NumpyArrayAdapter(arr)
        result = (np.array([[1.]]) * barr).masked_array()
        target = np.array([[1.]]) * arr

        np.testing.assert_array_equal(result, target)
        np.testing.assert_array_equal(result.mask, target.mask)

    def test_no_array_priority_attribute_present(self):
        arr = biggus.ConstantArray((3), 1.0)
        barr = biggus.NumpyArrayAdapter(arr)
        result = np.array([[1.]]) * barr
        target = np.array([[1.]]) * arr
        np.testing.assert_array_equal(result, target)


if __name__ == '__main__':
    unittest.main()
