# File for misc utilities
import math, re
from pathlib import Path

the = {
    'data': '',
    'show_help': False,
    'filepath': '',
    'dump': False,
    'nums': 512,
    'seed': 10019,
    'seperator': ',',
    'eg': None
};


def per(t, p):
    p = math.floor(((p or .5)*len(t))+.5)
    return t[max(1,min(len(t),p))]

def oo(t):
    print(str(t))
    return t

def coerce(s):
    s = float(s) if bool(re.search(r'\d', s)) else s
    return s

def csv(filepath: Path):
    filepath = Path(filepath);
    print("Exists criteria : ", filepath.exists())
    print("suffix : ", filepath.suffix)

    if not filepath.exists() or filepath.suffix != '.csv':
        print("File path does not exist OR File not csv, given path: ", filepath.absolute())
        return

    rows = []
    with open(filepath.absolute(), 'r', encoding='utf-8') as file:
        for row_no, line in enumerate(file):
            row = list(map(coerce, line.strip().split(the['seperator'])))
            rows.append(row)
    return rows
