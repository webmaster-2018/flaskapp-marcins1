#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tworzeniebazy.py
#
import os

from modele import *

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen])
    baza.commit()
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
