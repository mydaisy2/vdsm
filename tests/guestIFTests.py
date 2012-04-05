#
# Copyright 2012 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301  USA
#
# Refer to the README and COPYING files for full details of the license
#

import guestIF

from testrunner import VdsmTestCase as TestCaseBase


class TestGuestIF(TestCaseBase):

    def testfilterXmlChars(self):
        ALL_LEGAL = "Hello World"
        self.assertEqual(ALL_LEGAL, guestIF._filterXmlChars(ALL_LEGAL))
        TM = u"\u2122".encode('utf8')
        self.assertNotEqual(TM, guestIF._filterXmlChars(TM))
