import datetime
import time
import os
import argparse
import sys

# Parse args
parser = argparse.ArgumentParser('Set a timebox.')
parser.add_argument('minutes', help='Number of minutes to timebox.', type=int)
args = parser.parse_args()

class timebox:
	"""Timebox object."""
	def __init__(self, length=10):
		"""Optional timebox length argument. Default is 10."""
		self.start_time = None
		self.length = datetime.timedelta(minutes=length)
		self.finish_time = None
		self.notification_times = []

	def start(self):
		"""Start timebox now."""
		self.start_time = datetime.datetime.now()
		self.finish_time = self.start_time + self.length
		self.notification_times[:] = [n + self.start_time for n in self.notification_times]
		self.notification_times.append(self.finish_time)
		self.notification_times.sort()

	def add_notification(self, minute_list):
		"""Add notification alert at specified minutes remaining. minute_list argument is a list"""		
		for minute in minute_list:
			if minute < (self.length.seconds / 60):
				self.notification_times.append(datetime.timedelta(minutes=minute))
				self.notification_times.sort()
			else:
				pass

	def remove_notification(self, minute):
		"""Remove notification alert at specified minutes remaining."""
		td = datetime.timedelta(minutes=minute) + self.start_time
		if td in self.notification_times:
			self.notification_times.remove(td)
		else:
			pass

	def time_left(self):
		"""Returns time left."""
		time_now = datetime.datetime.now()
		return self.finish_time - time_now

	def print_time(self):
		"""Use self.time_left to sys.stdout.write to console."""
		t = self.time_left()
		sys.stdout.write("{:0<2d}:{:0<2d}\r".format(int(t.seconds / 60), t.seconds % 60))

	def check(self):
		"""Checks if notification[0] has been met and removes it if it has."""
		time_now = datetime.datetime.now()
		if time_now >= self.notification_times[0]:
			self.notify(self.notification_times[0])
			self.notification_times.pop(0)

	def notify(self, time):
		"""Handles the actual notification using system say."""
		if len(self.notification_times) > 0:
			os.system('say "{} minutes remaining"'.format(int(self.time_left().seconds / 60))) # Placeholder
		else:
			os.system('say "Timebox finished"')

def main():
	tb = timebox(args.minutes)
	tb.add_notification([5, 10, 15, 30, 60]) # Placeholder, should be automatically generated based on length or changed according to user
	tb.start()
	while len(tb.notification_times):
		sys.stdout.flush()
		tb.print_time()
		tb.check()
		time.sleep(0.5)

main()
