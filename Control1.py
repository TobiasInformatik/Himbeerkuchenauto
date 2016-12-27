import sys, tty, termios, os, readchar
import RPi.GPIO as PIN
import time

PIN.setmode(PIN.BOARD)

L = 23
R = 22
RW = 24
VW = 26

PIN.setup(L,PIN.OUT)
PIN.setup(R,PIN.OUT)
PIN.setup(RW,PIN.OUT)
PIN.setup(VW,PIN.OUT)

os.system('clear')

print ("Motorsteuerung")
print ("  Vorwärts: a")
print ("  Rückwärts: d")
print ("  Gerade: h")
print ("  Links: g")
print ("  NOTSTOP: f")
print ("  Motor AUS: s")
print ("PROGRAMM ENDE: x")

def getch():
	ch = readchar.readchar()
	return ch

while True:
	char= getch()
	if(char == "a"):
		PIN.output(VW,PIN.HIGH)
		PIN.output(RW,PIN.LOW)
		
	if(char == "s"):
		PIN.output(VW,PIN.LOW)
		PIN.output(RW,PIN.LOW)
		
	if(char == "d"):
		PIN.output(RW,PIN.HIGH)
		PIN.output(VW,PIN.LOW)
	
	if(char == "f"):
		PIN.output(VW,PIN.LOW)
		PIN.output(RW,PIN.LOW)
		PIN.output(L,PIN.LOW)
		PIN.output(R,PIN.LOW)
		
	if(char == "g"):
		PIN.output(L,PIN.HIGH)
		PIN.output(R,PIN.LOW)
		
	if(char == "h"):
		PIN.output(L,PIN.LOW)
		PIN.output(R,PIN.LOW)
		
	if(char == "j"):
		PIN.output(R,PIN.HIGH)
		PIN.output(L,PIN.LOW)
		
	if(char == "x"):
		PIN.output(VW,PIN.LOW)
		PIN.output(RW,PIN.LOW)
		PIN.output(L,PIN.LOW)
		PIN.output(R,PIN.LOW)
		time.sleep(0.5)
		PIN.cleanup
		break