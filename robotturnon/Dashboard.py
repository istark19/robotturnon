from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

print "done"

sensor_pin = 17
RPL.pinMode(17,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(17)
  PTW.state['d2'] = RPL.digitalRead(23)
  PTW.post()