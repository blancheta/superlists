#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

	os.environ['DJANGO_SETTINGS_MODULE'] = "superlists.settings"
	# sys.path.append('/home/aldazar/sites/staging.aldazar-superlists.ddns.net/source')
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)