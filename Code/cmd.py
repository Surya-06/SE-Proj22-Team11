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
  -e or --eg : Start-up example
  ''';
  print(help_msg);

def get_option_for_switch(i, args):
  if i+1 >= len(args):
    raise Exception("Invalid parameters. Please run again with '-h' for instructions");
  
  return args[i+1], i+1;

def parse_command_line():
  args = sys.argv[1:];
  i = 0;
  while i < len(args):
    if args[i] == '-h' or args[i] == '--help':
      the['show_help'] = True;
    elif args[i] == '-f' or args[i] == '--filepath':
      the['filepath'], i = get_option_for_switch(i, args);
    elif args[i] == '-d' or args[i] == '--dump':
      the['dump'], i = get_option_for_switch(i, args);
    elif args[i] == '-n' or args[i] == '--nums':
      the['nums'], i = get_option_for_switch(i, args);
    elif args[i] == '-s' or args[i] == '--seed':
      the['seed'], i = get_option_for_switch(i, args);
    elif args[i] == '-S' or args[i] == '--seperator':
      the['seperator'], i = get_option_for_switch(i, args);
    elif args[i] == '-e' or args[i] == '--eg':
      the['eg'], i = get_option_for_switch(i, args);
    else:
      raise Exception('WRONG OPTION: Please run with -h for help page.');
    i += 1;