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

from .X11PosChain import X11PosChain

class BeeCoin2Chain(X11PosChain):
    def __init__(chain, **kwargs):
        chain.name = 'BeeCoin2Chain'
        chain.code3 = 'BEE2'
        chain.address_version = '\x05'
        chain.script_addr_vers = '\x0b'
        chain.magic = '\x70\x35\x22\x05'
        X11PosChain.__init__(chain, **kwargs)

    datadir_conf_file_name = 'beecoinv2.conf'
    datadir_rpcport = 44466 
    datadir_p2port = 66644 
