#!/usr/bin/env python
import os
import sys

project_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(project_dir))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techblog.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
