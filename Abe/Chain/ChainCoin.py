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

class ChainCoin(BaseChain):
    """
    A blockchain that hashes block headers using the Chaincoin algorithm.
    The current implementation requires the chaincoin_hash module.
    """

    # POLICY_ATTRS = BaseChain.POLICY_ATTRS

    def __init__(chain, **kwargs):
        chain.name = 'ChainCoin'
        chain.code3 = 'CHC'
        chain.address_version = '\x1c'
        chain.script_addr_vers = '\x04'
        chain.magic = '\xa3\xd2\x7a\x03'
        super(ChainCoin, chain).__init__(**kwargs)

    def block_header_hash(chain, header):
        import chaincoin_hash
        return chaincoin_hash.getPoWHash(header)

    def ds_parse_transaction(chain, ds):
        def wrapped_ds_parse_transaction(vds, has_nTime=False):
            d = {}
            start_pos = vds.read_cursor
            d['version'] = vds.read_int32()
            if has_nTime:
                d['nTime'] = vds.read_uint32()
            n_vin = vds.read_compact_size()
            d['txIn'] = []
            for i in xrange(n_vin):
                d['txIn'].append(deserialize.parse_TxIn(vds))
            n_vout = vds.read_compact_size()
            d['txOut'] = []
            for i in xrange(n_vout):
                d['txOut'].append(deserialize.parse_TxOut(vds))
            d['lockTime'] = vds.read_uint32()
            if d['version'] > 1:
                d['tx-comment'] = vds.read_string()
            d['__data__'] = vds.input[start_pos:vds.read_cursor]
            return d
        return wrapped_ds_parse_transaction(ds, has_nTime=False)

    datadir_conf_file_name = 'chaincoin.conf'
    datadir_rpcport = 11995
    datadir_p2pport = 11994
    # start_time = 1394480376

