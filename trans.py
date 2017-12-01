#!/usr/bin/env python
import argparse
import pyperclip
import re
import time
from googletrans import Translator


def f(s):
    trans = Translator()
    sr = '.\n'.join([l.strip(' ') for l in re.split('\.|\?|!', s)])
    sr = sr.replace('et al.\n', 'et al.')
    sr = sr.replace('e.\ng.\n', 'e.g.')
    sr = sr.replace('i.\ne.\n', 'i.e.')
    sr = sr.replace('etc.\n', 'etc.')
    sr = re.sub(r'Fig\.\n([0-9]+)\.\n([0-9]+)', 'Fig.\g<1>.\g<2>', sr)
    sja = []
    # The maximum character limit on a single text is 15k.
    for l in sr.splitlines():
        if len(l) > 15000:
            print('this line is too long!')
        lja = trans.translate(l, dest='ja').text
        # time.sleep(0.01)
        sja.append(lja+'\n')
    sja = '\n'.join([l.strip() for l in sja])
    return sr, sja

def fj(s):
    return '。\n'.join(re.split('。|？', s))

def rs(s, splitter=f):
    s_cat = ' '.join(s.splitlines())
    ren, rja = splitter(s_cat)
    return ren, rja

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ja', '-j', action='store_true')
    parser.add_argument('--count', '-c', action='store_true')
    parser.add_argument('--output', '-o', default='output.txt')
    args = parser.parse_args()
    if args.ja:
        r = rs(pyperclip.paste(), splitter=fj)
    else:
        if args.count:
            print(len(pyperclip.paste().split('')))
        with open(args.output+'.en', 'w', encoding='utf8') as fen,  \
             open(args.output+'.ja', 'w', encoding='utf8') as fja:
            ren, rja = rs(pyperclip.paste(), splitter=f)
            fen.write(ren)
            fja.write(rja)
            r = ren + '\n' + rja
    print(r)
    pyperclip.copy(r)
