# Volatility
# Copyright (C) 2007-2013 Volatility Foundation
#
# This file is part of Volatility.
#
# Volatility is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Volatility is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Volatility.  If not, see <http://www.gnu.org/licenses/>.
#

"""
@author:       Andrew Case
@license:      GNU General Public License 2.0
@contact:      atcuno@gmail.com
@organization: 
"""

import volatility.obj as obj
import volatility.debug as debug
import volatility.plugins.linux.common as linux_common
import volatility.plugins.linux.plthook as linux_plthook
import volatility.plugins.linux.pslist as linux_pslist

try:
    import distorm3
except ImportError:
    debug.error("This plugin requres the distorm library to operate.")
    
class linux_apihooks(linux_pslist.linux_pslist):
    """Checks for userland apihooks"""

    def render_text(self, outfd, data):
        linux_common.set_plugin_members(self)
        self.table_header(outfd, [
                                  ("Pid", "7"),
                                  ("Name", "16"),
                                  ("Hook VMA", "40"),
                                  ("Hook Symbol", "24"),
                                  ("Hooked Address", "[addrpad]"),
                                  ("Type", "5"),
                                  ("Hook Address", "[addrpad]"),                    
                                  ("Hook Library", ""),
                                  ]) 

        for task in data:
            for hook_desc, sym_name, addr, hook_type, hook_addr, hookfuncdesc in task.apihook_info():
                self.table_row(outfd, task.pid, task.comm, hook_desc, sym_name, addr, hook_type, hook_addr, hookfuncdesc)


