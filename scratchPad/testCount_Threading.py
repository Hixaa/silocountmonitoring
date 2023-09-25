import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
i = 0

def set_interval(func, sec):
	def func_wrapper():
		set_interval(func, sec)
		func()
	t = threading.Timer(sec, func_wrapper)
	t.start()
	return t
	
def zeroI():
	global i
	print(i)
	i = 0

set_interval(zeroI, 1.0)
while True:
	GPIO.wait_for_edge(4, GPIO.RISING)
	i = i + 1

GPIO.cleanup()