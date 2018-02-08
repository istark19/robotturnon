from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

print "done"

sensor_pin = 17
RPL.pinMode(sensor_pin,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(sensor_pin)
  PTW.post()
