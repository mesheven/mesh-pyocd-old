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

from flash import Flash



flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
                                  0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
                                  0x6000f1a0, 0x47700ac0, 0x495b485c, 0x495c6001, 0x20006001, 0x49594770, 0x30f9f24c, 0x60083108, 
                                  0x49564770, 0x30f9f24c, 0x60083108, 0x47702000, 0x47702000, 0xb5004a51, 0x6810320c, 0xda012800, 
                                  0xffe2f7ff, 0x3108494d, 0x03c06808, 0xf24cd4fc, 0x600830f9, 0xf2486810, 0x43180304, 0x68106010, 
                                  0x3080f440, 0x68086010, 0xd4fc03c0, 0x43986810, 0x20006010, 0xb530bd00, 0x24004b40, 0x4605330c, 
                                  0x28006818, 0xf7ffda01, 0x4a3cffbf, 0x68113208, 0xd4fc03c8, 0x30f9f24c, 0xf1a56010, 0x0ae86500, 
                                  0xd30228ff, 0x6400f44f, 0x6819b2c0, 0x75f8f640, 0x250243a9, 0x00c0eb05, 0x0004ea40, 0x0001ea40, 
                                  0x68186018, 0x3080f440, 0x68106018, 0xd4fc03c0, 0xf0206818, 0x60180002, 0xbd302000, 0x45f0e92d, 
                                  0x2400460e, 0xd0010749, 0xe0002701, 0x4d232700, 0x0307f020, 0xf022350c, 0x68280207, 0xda012800, 
                                  0xff82f7ff, 0x3108491d, 0x03c06808, 0xf24cd4fc, 0x600830f9, 0xf0406828, 0x60280001, 0x0a01f04f, 
                                  0x06d6eb07, 0x6810e01f, 0x68086018, 0xd4fc03c0, 0x07c06808, 0xf8c1d001, 0x6810a000, 0xf8d36857, 
                                  0xf8d3c000, 0xea808004, 0xea87000c, 0x43380708, 0x6828d006, 0x0001f020, 0x20016028, 0x85f0e8bd, 
                                  0x32083308, 0x42a61c64, 0x6828d8dd, 0x0001f020, 0x20006028, 0x0000e7f2, 0x45670123, 0x40023c04, 
                                  0xcdef89ab, 0x00000000,
                                ],
               'pc_init'          : 0x20000043,
               'pc_eraseAll'      : 0x20000055,
               'pc_erase_sector'  : 0x20000097,
               'pc_program_page'  : 0x200000FD,
               'static_base'      : 0x20000200,
               'begin_data'       : 0x20001000, # Analyzer uses a max of 2 KB data (512 pages * 4 bytes / page)
               'page_buffers'    : [0x20001000, 0x20001800],   # Enable double buffering
               'begin_stack'      : 0x20002800,
               'min_program_length' : 8,
               'analyzer_supported' : True,
               'analyzer_address' : 0x20003000 # Analyzer 0x20003000..0x20003600
              };


class Flash_stm32l486(Flash):

    def __init__(self, target):
        super(Flash_stm32l486, self).__init__(target, flash_algo)