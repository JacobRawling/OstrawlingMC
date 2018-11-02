#coding=utf-8

"""
@Brief Here can go any system checks that need making
"""

# Check python version
import sys
try:
  assert sys.version_info >= (3,0)
except AssertionError:
  print("\033[1m\033[31;5;31mError:\033[0m Please use python 3. The future is now 😘")
  exit(-1)