#!/usr/bin/env python
import argparse
import pyperclip
import re


def f(s):
    sr = '.\n'.join([l.strip(' ') for l in re.split('\.|\?|!', s)])
    sr = sr.replace('et al.\n', 'et al.')
    sr = sr.replace('e.\ng.\n', 'e.g.')
    sr = sr.replace('i.\ne.\n', 'i.e.')
    sr = sr.replace('etc.\n', 'etc.')
    sr = re.sub(r'Fig\.\n([0-9]+)\.\n([0-9]+)', 'Fig.\g<1>.\g<2>', sr)
    return sr

def fj(s):
    return '。\n'.join(re.split('。|？', s))

def rs(s, splitter=f):
    s_cat = ' '.join(s.splitlines())
    return splitter(s_cat)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ja', '-j', action='store_true')
    parser.add_argument('--count', '-c', action='store_true')
    args = parser.parse_args()
    if args.ja:
        r = rs(pyperclip.paste(), splitter=fj)
    else:
        if args.count:
            print(len(pyperclip.paste().split('')))
        r = rs(pyperclip.paste(), splitter=f)
    print(r)
    pyperclip.copy(r)
