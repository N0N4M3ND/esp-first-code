import time

import requests as req

esp = "http://192.168.4.114:6006"

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

time.sleep(1)

led1on()

time.sleep(1)

led2on()

time.sleep(1)

led3on()

time.sleep(1)

led4on()

time.sleep(1)

led5on()

time.sleep(1)

led6on()

#off

led0off()

time.sleep(1)

led1off()

time.sleep(1)

led2off()

time.sleep(1)

led3off()

time.sleep(1)

led4off()

time.sleep(1)

led5off()

time.sleep(1)

led6off()

time.sleep(1)
