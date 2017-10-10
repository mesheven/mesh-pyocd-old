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

from cortex_m import CortexM
from .memory_map import (FlashRegion, RamRegion, MemoryMap)
import logging

DBGMCU_CR      = 0xE0042004
DBGMCU_APB1_CR1 = 0xE0042008
DBGMCU_APB1_CR2 = 0xE004200C
DBGMCU_APB2_CR  = 0xE0042010

#0000 0000 0000 0000 0000 0000 0000 0000
DBGMCU_VAL      = 0x00000000
#1000 0110 1110 0000 0001 1100 0011 1111
DBGMCU_APB1_VAL1 = 0x86E01C3F
#0000 0000 0000 0000 0000 0000 0010 0001
DBGMCU_APB1_VAL2 = 0x00000021
#0000 0000 0000 0111 0010 1000 0000 0000
DBGMCU_APB2_VAL  = 0x00072800


class STM32L486(CortexM):

    memoryMap = MemoryMap(
        FlashRegion(    start=0x08000000,  length=0x100000,      blocksize=0x0800, isBootMemory=True),
        RamRegion(      start=0x20000000,  length=0x20000)
        )
    
    def __init__(self, transport):
        super(STM32L486, self).__init__(transport, self.memoryMap)

    def init(self):
    	logging.debug('stm32l486 init')
        CortexM.init(self)
        self.writeMemory(DBGMCU_CR, DBGMCU_VAL)
        self.writeMemory(DBGMCU_APB1_CR1, DBGMCU_APB1_VAL1)
        self.writeMemory(DBGMCU_APB1_CR2, DBGMCU_APB1_VAL2)       
        self.writeMemory(DBGMCU_APB2_CR, DBGMCU_APB2_VAL)
