import time

import requests as req

esp = "http://188.169.2.234:6006"

timedelay = 0

#off

def led0off():
    req.get(esp+"/0/off")

def led1off():
    req.get(esp+"/1/off")
    
def led2off():
    req.get(esp+"/2/off")
    
def led3off():
    req.get(esp+"/3/off")
    
def led4off():
    req.get(esp+"/4/off")
    
def led5off():
    req.get(esp+"/5/off")
    
def led6off():
    req.get(esp+"/6/off")

def led0on():
    req.get(esp+"/0/on")

def led1on():
    req.get(esp+"/1/on")
    
def led2on():
    req.get(esp+"/2/on")
    
def led3on():
    req.get(esp+"/3/on")
    
def led4on():
    req.get(esp+"/4/on")
    
def led5on():
    req.get(esp+"/5/on")
    
def led6on():
    req.get(esp+"/6/on")

#code starts now

led0on()

time.sleep(timedelay)

led0off()

time.sleep(timedelay)

led1on()

time.sleep(timedelay)

led1off()

time.sleep(timedelay)

led2on()

time.sleep(timedelay)

led2off()

time.sleep(timedelay)

led3on()

time.sleep(timedelay)

led3off()

time.sleep(timedelay)

led4on()

time.sleep(timedelay)

led4off()

time.sleep(timedelay)

led5on()

time.sleep(timedelay)

led5off()

time.sleep(timedelay)

led6on()

time.sleep(timedelay)

led6off()

time.sleep(timedelay)
