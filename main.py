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

## Parse args
parser = argparse.ArgumentParser('Set a timebox.')
parser.add_argument('minutes', help="Number of minutes to timebox.", type=int)
parser.add_argument('-s', help='Silent timebox.', action="store_true")
parser.add_argument('--song', help='Sing a song when finished.', action="store_true")
parser.add_argument('-a', help="Alerts throughout timebox.", action="store_true")
parser.add_argument('-r', help="Timebox alert is a randomized phrase.", action="store_true")
parser.add_argument('--test', help="Run 10 second timebox for testing purposes.", action="store_true")
args = parser.parse_args()

## Time
minutes = int(args.minutes)

count = minutes * 60

## Test Mode
if args.test:
	count = 10

## Countdown
while count >= 0:
	sys.stdout.flush()
	minute = int(count / 60)
	second = count % 60
	sys.stdout.write("{:0>2d}:{:0>2d}\r".format(minute, second))
	count -= 1
	time.sleep(1)

## End Result
print "Timebox finished"
if args.s:
	pass
elif args.song:
	os.system('say "{0}"'.format(songs[randint(0, len(songs) - 1)]))
elif args.r:
	os.system('say "{0}"'.format(phrases[randint(0, len(phrases) - 1)]))
else:
	os.system('say {0}'.format(phrases[0]))