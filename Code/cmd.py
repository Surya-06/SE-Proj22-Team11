# command line arg parser

import sys

from utils import the;

def print_help_message():
  help_msg = '''
  Please use any of the below options and run again:
  -h OR --help : Displays this message
  -f <FILEPATH> OR --filename <FILEPATH> : (Required) Provides filepath for data.
  -d OR --dump : Set True or False to print stack dump on test failure
  -n or --nums : Set number of nums to keep
  -s or --seed : Set random number seed
  -S or --seperator : Set field seperator
  ''';
  print(help_msg);

def parse_command_line():
  args = sys.argv[1:];
  i = 0;
  while i < len(args):
    if args[i] == '-h' or args[i] == '--help':
      the['show_help'] = True;
    elif args[i] == '-f' or args[i] == '--filepath':
      i = i+1
      the['filepath'] = args[i];
    elif args[i] == '-d' or args[i] == '--dump':
      i = i+1
      the['dump'] = args[i]
    elif args[i] == '-n' or args[i] == '--nums':
      i = i+1
      the['nums'] = args[i]  
    elif args[i] == '-s' or args[i] == '--seed':
      i = i+1
      the['seed'] = args[i]
    elif args[i] == '-S' or args[i] == '--seperator':
      i = i+1
      the['seperator'] = args[i]          
    else:
      raise Exception('WRONG OPTION: Please run with -h for help page.');
    i += 1;