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

from . import RouletteChain
from .. import deserialize

class RouletteCoinChain(RouletteChain):
    """
    A blockchain that hashes block headers using the Roulette algorithm.
    The current implementation requires the roulette_hash module.
    """

    # POLICY_ATTRS = BaseChain.POLICY_ATTRS

    def __init__(chain, **kwargs):
        chain.name = 'RouletteCoinChain'
        super(RouletteCoinChain, chain).__init__(**kwargs)

    def ds_parse_block_header(vds):
        d = {}
        header_start = vds.read_cursor
        d['version'] = vds.read_int32()
        d['hashPrev'] = vds.read_bytes(32)
        d['hashMerkleRoot'] = vds.read_bytes(32)
        d['nTime'] = vds.read_uint32()
        d['nBits'] = vds.read_uint32()
        d['nNonce'] = vds.read_uint32()
        d['nReserved1'] = vds.read_uint32()
        d['nReserved2'] = vds.read_uint32()
        header_end = vds.read_cursor
        d['__header__'] = vds.input[header_start:header_end]
        return d

    def ds_serialize_block_header(chain, ds, block):
        ds.write_int32(block['version'])
        ds.write(block['hashPrev'])
        ds.write(block['hashMerkleRoot'])
        ds.write_uint32(block['nTime'])
        ds.write_uint32(block['nBits'])
        ds.write_uint32(block['nNonce'])
        ds.write_uint32(block['nReserved1'])
        ds.write_uint32(block['nReserved2'])

