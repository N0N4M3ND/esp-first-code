import requests as req

import time

esp = "http://188.169.2.234:6006"

# variables

delay0 = 0

delay05 = 0.5

delay1 = 1

delay2 = 2

delay25 = 2.5

delay3 = 3

delay4 = 4

delay5 = 5

#off

def led0off():
    req.get(esp+"/0/off")
    print("0off")

def led1off():
    req.get(esp+"/1/off")
    print("1off")

def led2off():
    req.get(esp+"/2/off")
    print("2off")

def led3off():
    req.get(esp+"/3/off")
    print("3off")

def led4off():
    req.get(esp+"/4/off")
    print("4off")

def led5off():
    req.get(esp+"/5/off")
    print("5off")

def led6off():
    req.get(esp+"/6/off")
    print("6off")

def led0on():
    req.get(esp+"/0/on")
    print("0on")

def led1on():
    req.get(esp+"/1/on")
    print("1on")

def led2on():
    req.get(esp+"/2/on")
    print("2on")

def led3on():
    req.get(esp+"/3/on")
    print("3on")

def led4on():
    req.get(esp+"/4/on")
    print("4on")

def led5on():
    req.get(esp+"/5/on")
    print("5on")

def led6on():
    req.get(esp+"/6/on")
    print("6on")

#code starts now

# clear lights

led0off()

time.sleep(delay0)

led1off()

time.sleep(delay0)

led2off()

time.sleep(delay0)

led3off()

time.sleep(delay0)

led4off()

time.sleep(delay0)

led5off()

time.sleep(delay0)

led6off()

time.sleep(delay0)

# lights

# loop from here

def lights():

# red on

    led6on()
    time.sleep(delay5)

# yellow on

    led5on()
    time.sleep(delay5)

# red & yellow off

    led6off()
    time.sleep(delay0)

    led5off()
    time.sleep(delay0)

# green on & flash

    led4on()
    time.sleep(delay5)

    led4off()
    time.sleep(delay05)

    led4on()
    time.sleep(delay05)

    led4off()
    time.sleep(delay05)

    led4on()
    time.sleep(delay05)

    led4off()
    time.sleep(delay05)

# yellow after flash

    led5on()
    time.sleep(delay5)

    led5off()
    time.sleep(delay0)

    lights()

lights()

# preperations for another

#led4off()
#time.sleep(delay0)

#led5off()
#time.sleep(delay0)

#led6off()
#time.sleep(delay0)

