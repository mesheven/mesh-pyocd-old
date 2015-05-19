"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash, PageInfo, DEFAULT_PAGE_PROGRAM_WEIGHT, DEFAULT_PAGE_ERASE_WEIGHT



flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
                                  0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
                                  0xf1a14601, 0xf44f6200, 0xf04f3380, 0x429a30ff, 0x0b90d201, 0x4a494770, 0x429a440a, 0x2004d201, 
                                  0x4a474770, 0xf5b14411, 0xd2f92f60, 0xeb002005, 0x47704051, 0x49434844, 0x49446001, 0x20006001, 
                                  0x49414770, 0x310820f1, 0x20006008, 0x20004770, 0x4a3d4770, 0x320cb500, 0x28006810, 0xf7ffda01, 
                                  0x4939ffe9, 0x68083108, 0xd4fc03c0, 0xf0406810, 0x60100004, 0xf4406810, 0x60103080, 0x03c06808, 
                                  0x6810d4fc, 0x0004f020, 0x20006010, 0xb530bd00, 0x46024d2d, 0x6828350c, 0xda012800, 0xffcaf7ff, 
                                  0x34084c29, 0x03c86821, 0x4610d4fc, 0xffa8f7ff, 0x22026829, 0x0178f021, 0x00c0eb02, 0x0001ea40, 
                                  0x68286028, 0x3080f440, 0x68206028, 0xd4fc03c0, 0xf0206828, 0x60280002, 0xbd302000, 0x4f1ab5f0, 
                                  0x370c2400, 0x68384603, 0x2800460e, 0xf7ffda01, 0x4d15ffa1, 0x1101f240, 0x68283508, 0xd4fc03c0, 
                                  0x4308e014, 0x88106038, 0x68288018, 0xd4fc03c0, 0xf8b38810, 0x4560c000, 0x6838d005, 0x0001f020, 
                                  0x20016038, 0x1c9bbdf0, 0x1c641c92, 0xebb46838, 0xd3e60f56, 0x60384388, 0xbdf02000, 0xf7ff0000, 
                                  0xf7fe0000, 0x45670123, 0x40023c04, 0xcdef89ab, 0x00000000,  
                                ],
               'pc_init'          : 0x20000063,
               'pc_eraseAll'      : 0x20000073,
               'pc_erase_sector'  : 0x200000AF,
               'pc_program_page'  : 0x200000FD,
               'static_base'      : 0x20000200,               
               'begin_data'       : 0x20001000, # Analyzer uses a max of 256 B data (64 pages * 4 bytes / page)
               'begin_stack'      : 0x20001000,
               'page_size'        : 16384,
               'analyzer_supported' : True,
               'analyzer_address' : 0x20006000 # Analyzer 0x20006000..0x20006600
              };

              
class Flash_stm32f405(Flash):
    
    def __init__(self, target):
        super(Flash_stm32f405, self).__init__(target, flash_algo)

    def getPageInfo(self, addr):
        info = PageInfo()
        if addr < 0x08010000:
            info.erase_weight = DEFAULT_PAGE_ERASE_WEIGHT
            info.program_weight = DEFAULT_PAGE_PROGRAM_WEIGHT
            info.size = 0x4000
        elif addr < 0x08020000:
            info.erase_weight = DEFAULT_PAGE_ERASE_WEIGHT * 4
            info.program_weight = DEFAULT_PAGE_PROGRAM_WEIGHT * 4
            info.size = 0x10000
        else:
            info.erase_weight = DEFAULT_PAGE_ERASE_WEIGHT * 8
            info.program_weight = DEFAULT_PAGE_PROGRAM_WEIGHT * 8
            info.size = 0x20000

        return info


