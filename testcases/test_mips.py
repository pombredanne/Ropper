# coding=utf-8
#
# Copyright 2014 Sascha Schirra
#
# This file is part of Ropper.
#
# Ropper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ropper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ropper.loaders.loader import *
from ropper.rop import Ropper
from ropper.arch import *

import unittest

class ELF_Mips(unittest.TestCase):

    def setUp(self):
        self.file = Loader.open('test-binaries/ls-mipsel')

    def test_general(self):
        self.assertEqual(self.file.arch, MIPS)
        self.assertEqual(self.file.type, Type.ELF)


    def test_gadgets(self):
        ropper = Ropper()
        gadgets = ropper.searchGadgets(self.file)

        gadget = gadgets[0]
        self.assertGreater(len(gadgets), 2100)
        self.assertEqual(gadget.lines[0][0] + self.file.imageBase, gadget.address)
        self.assertEqual(gadget.imageBase, 0x400000)
        self.file.imageBase = 0x0
        self.assertEqual(gadget.imageBase, 0x0)
        self.file.imageBase = None
        self.assertEqual(gadget.imageBase, 0x400000)


if __name__ == '__main__':
    unittest.main()
