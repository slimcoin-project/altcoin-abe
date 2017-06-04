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
from .. import deserialize

class RouletteChain(BaseChain):
    """
    A blockchain that hashes block headers using the RouletteCoin algorithm.
    The current implementation requires the roulette_hash module.
    """

    # POLICY_ATTRS = BaseChain.POLICY_ATTRS

    def __init__(chain, **kwargs):
        chain.name = 'RouletteChain'
        super(RouletteChain, chain).__init__(**kwargs)

    def block_header_hash(chain, header):
        import roulette_hash
        return roulette_hash.getPoWHash(header)

