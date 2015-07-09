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

from cortex_m import CortexM, DHCSR, DBGKEY, C_DEBUGEN, C_MASKINTS, C_STEP, DEMCR, VC_CORERESET, NVIC_AIRCR, NVIC_AIRCR_VECTKEY, NVIC_AIRCR_SYSRESETREQ
from pyOCD.target.target import TARGET_RUNNING, TARGET_HALTED
import logging

DBGMCU_CR      = 0xE0042004
DBGMCU_APB1_CR = 0xE0042008
DBGMCU_APB2_CR = 0xE004200C

#0000 0000 0000 0000 0000 0000 0000 0000
DBGMCU_VAL      = 0x00000000
#0000 0110 1110 0000 0001 1101 1111 1111
DBGMCU_APB1_VAL = 0x06E01DFF

#0000 0000 0000 0111 0000 0000 0000 0011
DBGMCU_APB2_VAL = 0x00070003


class STM32F405(CortexM):

    memoryMap = MemoryMap(
        FlashRegion(    start=0x08000000,  length=0x100000,      blocksize=0x4000, isBootMemory=True),
        RamRegion(      start=0x20000000,  length=0x20000)
        )
    
    def __init__(self, transport):
        super(STM32F405, self).__init__(transport)

    def init(self):
    	logging.debug('stm32f405 init')
        CortexM.init(self)
        self.writeMemory(DBGMCU_CR, DBGMCU_VAL)
        self.writeMemory(DBGMCU_APB1_CR, DBGMCU_APB1_VAL)
        self.writeMemory(DBGMCU_APB2_CR, DBGMCU_APB2_VAL)



