import urequests as requests
import machine


p0 = machine.Pin(2, machine.Pin.OUT)


def toggle(p):
    p.value(not p.value())


def gsx_req(msg):
    user = "JockDaRock"
    url = "http://gsx-clust-external-12qq4jfx2i278-442547460.us-west-1.elb.amazonaws.com:8080/function/hello-python"

    payload = "%s's LED State: %s" % (user, msg)

    r = requests.post(url, data=payload)
    return r


def callback(p):
    if p.value() == 0:
        msg = "LED on"
        print(gsx_req(msg))
    else:
        msg = "LED off"
        print(gsx_req(msg))

p0.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=callback)
