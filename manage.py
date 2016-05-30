#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from superlists import settings as mysettings

if __name__ == "__main__":

	os.environ['DJANGO_SETTINGS_MODULE'] = "superlists.settings"
	sys.path.append('/source')

	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)


