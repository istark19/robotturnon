from setup import RPL
import post_to_web as PTW # see post_to_web.py for instructions

sensor_pin = 17
RPL.pinMode(17,RPL.INPUT)

while True:
  PTW.state['d1'] = RPL.digitalRead(17)
  PTW.post()
