# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from . import BaseChain

class X13Chain(BaseChain):
    """
    A blockchain that hashes block headers using the X13 algorithm.
    The current implementation requires the x13_hash module.
    https://github.com/mindfox/x13-hash
    """

    def block_header_hash(chain, header):
        import x13_hash
        return x13_hash.getPoWHash(header)
