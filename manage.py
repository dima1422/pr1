#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pr1.settings")
    a=10
    c=1
    d=1
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
# a little changes