#!/usr/bin/python
import common
from subprocess import check_output

uci_path = '/sbin/uci'

def get(*args):
  args = list(args)
  args.insert(0, "get")
  try:
    return run(args)
  except subprocess.CalledProcessError, e:
    if e.output == 'uci: Entry not found':
      return None
    else:
      raise

def set(*args):
  args = list(args)
  args.insert(0, "set")
  return run(args)

def commit(*args):
  args = list(args)
  args.insert(0, "commit")
  return run(args)

def validate(string):
  if len(string) > 200:
    raise Exception('String input to UCI too long.')
  if string.find('\00') != -1:
    raise Exception('Invalid input: contains null bytes.')

def run(args_list):
  args_list.insert(0, uci_path)
  map(validate, args_list)
  return check_output(args_list).strip()
