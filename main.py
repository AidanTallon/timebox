import sys
import time
import os
import argparse
from random import randint

## Random phrases
phrases = ["Timebox finished",
	"Time is up",
	"You have run out of time",
	"Danger! There is no time",
	"My time is up"]

## Random songs
songs = ["Danger! Danger! High Voltage! When we touch. When we kiss.",
	"Tommy used to work on the docks. Union's been on strike, he's down on his luck. It's tough, so tough.",
	"I want to know what love is. I want you to show me.",
	"I'm bringing sexy back."]

## When to alert user of time left. Only alerts that are less than half of the timebox length are used
alerts = [60, 300, 600, 900, 1800]

## Parse args
parser = argparse.ArgumentParser('Set a timebox.')
parser.add_argument('minutes', help="Number of minutes to timebox.", type=int)
parser.add_argument('-s', help='Silent timebox.', action="store_true")
parser.add_argument('--song', help='Sing a song when finished.', action="store_true")
parser.add_argument('-a', help="Alerts throughout timebox.", action="store_true")
parser.add_argument('-r', help="Timebox alert is a randomized phrase.", action="store_true")
parser.add_argument('--test', help="Test mode reduces sleep time", action="store_true")
args = parser.parse_args()

## Main program loop
def main():
	## Check if test mode
	count = int(args.minutes) * 60
	if args.test:
		countdown(count, test=True)
	else:
		countdown(count)
	notification_end()

## Countdown loop
def countdown(c, test=False):
	## used for testing purposes
	if test is True:
		n = 0.05
	else:
		n = 1

	while c >= 0:
		write(c)
		c -= 1
		## halfway mark
		if (c == args.minutes * 30) or (c in alerts and c < args.minutes * 30):
			## needs to be async
			notification_duration(c)
		time.sleep(n)

## Writes time remaining to terminal
def write(c):
	m = int(c / 60)
	s = c % 60
	sys.stdout.flush()
	sys.stdout.write("{:0>2d}:{:0>2d}\r".format(m, s))

## Notification that timebox finished
def notification_end():
	print "Timebox finished"
	if args.s:
		pass
	elif args.song:
		os.system('say "{0}"'.format(songs[randint(0, len(songs) - 1)]))
	elif args.r:
		os.system('say "{0}"'.format(phrases[randint(0, len(phrases) - 1)]))
	else:
		os.system('say "{0}"'.format(phrases[0]))

## Notification of time remaining
def notification_duration(c):
	if args.a is True and args.s is False:
		m = int(c / 60)
		if m == 1:
			msg = "1 minute remaining."
		else:
			msg = "{0} minutes remaining.".format(m)
		os.system('say "{0}"'.format(msg))


main()