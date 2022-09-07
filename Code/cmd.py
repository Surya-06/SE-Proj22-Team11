# command line arg parser

import sys

from utils import the;

def printHelpMessage():
  help_msg = '''
  Please use any of the below options and run again:
  -h OR --help : Displays this message
  -f <FILEPATH> OR --filename <FILEPATH> : (Required) Provides filepath for data.
  ''';
  print(help_msg);

def parseCommandLine():
  args = sys.argv[1:];
  i = 0;
  while i < len(args):
    if args[i] == '-h' or args[i] == '--help':
      the['show_help'] = True;
    elif args[i] == '-f' or args[i] == '--filepath':
      i = i+1
      the['filepath'] = args[i];
    else:
      raise Exception('WRONG OPTION: Please run with -h for help page.');
    i += 1;