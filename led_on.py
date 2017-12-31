from uio     import Uio
import numpy as np
import time
import signal

class  LED:
    def __init__(self):
        self.uio  = Uio('uio1')
        self.regs = self.uio.regs()
        self.regs.write_word(4, 0)
        self.pattern = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02]
        self.index   = 0
        
    def run(self):
        self.regs.write_word(0, self.pattern[self.index])
        if self.index < len(self.pattern)-1:
            self.index = self.index + 1
        else:
            self.index = 0;

if __name__ == '__main__':
    led  = LED()

    for i in range(100):
        led.run()
        time.sleep(0.1)
        
