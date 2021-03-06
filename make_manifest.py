#! /usr/bin/env python

import os


def main():
    files = sorted(set([x.strip() for x in os.popen("git ls-files")])
                   - set(["make_manifest.py", "Makefile", ".gitignore"]))

    f = open("MANIFEST.in", "w")
    for x in files:
        f.write("include %s\n" % x)
    f.close()


if __name__ == '__main__':
    main()
