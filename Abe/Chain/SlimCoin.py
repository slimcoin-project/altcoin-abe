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

# from .DcryptChain import DcryptChain
# from .. import deserialize


# class SlimCoin(DcryptChain):
#     """
#     A blockchain with proof-of-stake as in Peercoin.
#     """
#     def __init__(chain, **kwargs):
#         chain.name = 'SlimCoin'
#         chain.code3 = 'SLM'
#         chain.address_version = '\x3f'
#         chain.script_addr_vers = '\x7d'
#         chain.magic = '\x6e\x8b\x92\xa5'
#         chain.decimals = 8
#         DcryptChain.__init__(chain, **kwargs)

#     def ds_parse_transaction(chain, ds):
#         return deserialize.parse_Transaction(ds, has_nTime=True)

#     def transaction_hash(chain, binary_tx):
#         return util.sha256(binary_tx)


#     def ds_parse_block(chain, ds):
#         d = DcryptChain.ds_parse_block(chain, ds)
#         d['block_sig'] = ds.read_bytes(ds.read_compact_size())
#         return d

#     datadir_conf_file_name = "slimcoin.conf"
#     datadir_rpcport = 41683
#     datadir_port = 41682

from .PpcPosChain import PpcPosChain
from .. import deserialize
from .. import util


class SlimCoin(PpcPosChain):
    """
    A blockchain that hashes block headers using the Dcrypt algorithm.
    The current implementation requires the dcrypt_hash module.
    """

    # POLICY_ATTRS = BaseChain.POLICY_ATTRS

    def __init__(chain, **kwargs):
        chain.name = 'SlimCoin'
        chain.code3 = 'SLM'
        chain.address_version = '\x3f'
        chain.script_addr_vers = '\x7d'
        chain.magic = '\x6e\x8b\x92\xa5'
        chain.decimals = 8
        PpcPosChain.__init__(chain, **kwargs)

    def block_header_hash(chain, header):
        import dcrypt_hash
        return dcrypt_hash.getPoWHash(header)

    def transaction_hash(chain, binary_tx):
        return util.sha256(binary_tx)

    def ds_parse_block(chain, ds):
        d = PpcPosChain.ds_parse_block(chain, ds)
        d['block_sig'] = ds.read_bytes(ds.read_compact_size())
        return d

    def ds_parse_block_header(chain, vds):
        d = {}
        header_start = vds.read_cursor
        d['version'] = vds.read_int32()
        d['hashPrev'] = vds.read_bytes(32)
        d['hashMerkleRoot'] = vds.read_bytes(32)
        d['nTime'] = vds.read_uint32()
        d['nBits'] = vds.read_uint32()
        d['nNonce'] = vds.read_uint32()

        d['fProofOfBurn'] = vds.read_boolean()
        d['hashBurnBlock'] = vds.read_bytes(32)
        d['burnHash'] = vds.read_bytes(32)
        d['burnBlkHeight'] = vds.read_uint32()
        d['burnCTx'] = vds.read_uint32()
        d['burnCTxOut'] = vds.read_uint32()
        d['nEffectiveBurnCoins'] = vds.read_int64()

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

        ds.write_boolean(block['fProofOfBurn'])
        ds.write(block['hashBurnBlock'])
        ds.write(block['burnHash'])
        ds.write_uint32(block['burnBlkHeight'])
        ds.write_uint32(block['burnCTx'])
        ds.write_uint32(block['burnCTxOut'])
        ds.write_int64(block['nEffectiveBurnCoins'])

    def ds_parse_transaction(chain, ds):
        def wrapped_ds_parse_transaction(vds, has_nTime=True):
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
            d['__data__'] = vds.input[start_pos:vds.read_cursor]
            return d
        return wrapped_ds_parse_transaction(ds, has_nTime=True)
