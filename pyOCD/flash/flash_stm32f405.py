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
                                  0xf1a14601, 0xf44f6200, 0xf04f3380, 0x429a30ff, 0x0b90d201, 0x4a584770, 0x429a440a, 0x2004d201, 
                                  0x4a564770, 0xf5b14411, 0xd2f92f60, 0xeb002005, 0x47704051, 0x49524853, 0x49536001, 0x20006001, 
                                  0x49504770, 0x310820f1, 0x20006008, 0x20004770, 0x4a4c4770, 0x320cb500, 0x28006810, 0xf7ffda01, 
                                  0x4948ffe9, 0x68083108, 0xd4fc03c0, 0xf4206810, 0xf0407040, 0x60100004, 0xf4406810, 0x60103080, 
                                  0x03c06808, 0x6810d4fc, 0x0004f020, 0x20006010, 0xb530bd00, 0x46024d3b, 0x6828350c, 0xda012800, 
                                  0xffc8f7ff, 0x34084c37, 0x03c86821, 0x4610d4fc, 0xffa6f7ff, 0x22026829, 0x715ef421, 0x00c0eb02, 
                                  0x0001ea40, 0x7000f440, 0x68286028, 0x3080f440, 0x68206028, 0xd4fc03c0, 0xf0206828, 0x60280002, 
                                  0xbd302000, 0x4e27b5f0, 0x360c2400, 0x68304603, 0x2800460d, 0xf7ffda01, 0x4922ff9d, 0x68083108, 
                                  0xd4fc03c0, 0xf4206830, 0x60307040, 0x3701f240, 0x2c01f240, 0x6830e010, 0x000cea40, 0x68106030, 
                                  0x68086018, 0xd4fc03c0, 0xf8d36810, 0x4570e000, 0x1d1bd117, 0x1c641d12, 0x0f95ebb4, 0x07a8d3eb, 
                                  0x6830d014, 0x1401f240, 0x7040f420, 0x60304320, 0x80188810, 0x03c06808, 0x8810d4fc, 0x42888819, 
                                  0x6830d004, 0x603043b8, 0xbdf02001, 0x43b86830, 0x20006030, 0x0000bdf0, 0xf7ff0000, 0xf7fe0000, 
                                  0x45670123, 0x40023c04, 0xcdef89ab, 0x00000000,   
                                ],
               'pc_init'          : 0x20000063,
               'pc_eraseAll'      : 0x20000073,
               'pc_erase_sector'  : 0x200000B3,
               'pc_program_page'  : 0x20000105,
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


