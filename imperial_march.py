#!/usr/bin/env python

import time

from random import randint



import unicornhat as uh



tone_values = {
'c': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'd': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'e': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'f': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'g': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'gS': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'a': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'aS': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'b': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'cH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'cH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'cSH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'dH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'dSH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}, 
'eH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)},
'fH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)},
'fSH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)},
'gH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)},
'gSH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)},
'aH': {'r': randint(10, 255),'g': randint(10, 255),'b': randint(10, 255)}
}

uh.set_layout(uh.PHAT)
uh.rotation(0)
uh.brightness(0.8)
width,height=uh.get_shape()


def beep(tone, timer):
    for key in tone_values:
        if key == tone:
            value = tone_values[key]
            for x in range(8):
                for y in range(4):
                   uh.set_pixel(x, y, value['r'], value['g'], value['b']) 
    uh.show()   
    time.sleep(timer)
    uh.clear()
    for x in range(8):
       for y in range(4):
          uh.set_pixel(x, y, 0, 0, 0) 
    uh.show()   
    time.sleep(0.05)

#Light it up, bro!
beep('a', 0.5)
beep('a', 0.5)
beep('a', 0.5)
beep('f', 0.35)
beep('cH', 0.15)
beep('a', 0.5)
beep('f', 0.35)
beep('cH', 0.15)
beep('a', 1)
#first bit
beep('eH', 0.5)
beep('eH', 0.5)
beep('eH', 0.5)
beep('fH', 0.35)
beep('cH', 0.15)
beep('gS', 0.5)
beep('f', 0.35)
beep('cH', 0.15)
beep('a', 1)
#second bit...
beep('aH', 0.5)
beep('a', 0.35)
beep('a', 0.15)
beep('aH', 0.5)
beep('gSH', 0.25)
beep('gH', 0.25)
beep('fSH', 0.125)
beep('fH', 0.125)
beep('fSH', 0.25)
time.sleep(0.25)
beep('aS', 0.25)
beep('dSH', 0.5)
beep('dH', 0.25)
beep('cSH', 0.25)
#start of the interesting bit
beep('cH', 0.125)
beep('b', 0.125)
beep('cH', 0.25)
time.sleep(0.25)
beep('f', 0.125)
beep('gS', 0.5)
beep('f', 0.375)
beep('a', 0.125)
beep('cH', 0.5)
beep('a', 0.375)
beep('cH', 0.125)
beep('eH', 1)
#more interesting stuff (this doesn't quite get it right somehow)
beep('aH', 0.5)
beep('a', 0.35)
beep('a', 0.15)
beep('aH', 0.5)
beep('gSH', 0.25)
beep('gH', 0.25)
beep('fSH', 0.125)
beep('fH', 0.125)
beep('fSH', 0.25)
time.sleep(0.25)
beep('aS', 0.25)
beep('dSH', 0.5)
beep('dH', 0.25)
beep('cSH', 0.25)
#repeat... repeat
beep('cH', 0.125)
beep('b', 0.125)
beep('cH', 0.25)
time.sleep(0.25)
beep('f', 0.25)
beep('gS', 0.5)
beep('f', 0.375)
beep('cH', 0.125)
beep('a', 0.5)
beep('f', 0.375)
beep('c', 0.125)
beep('a', 1)  
#and we're done \o/    
