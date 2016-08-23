#!/usr/bin/python
import sys
import time

l2n = dict(zip("aAeEiIlLoOsStTgGbB", "443311110055776668"))  # case sensitive


def letterToNumber(l):
    if l in l2n:
        l = l2n[l]
    return l


def changeCase(l):
    if l.islower():
        l = l.upper()
    else:
        l = l.lower()
    return l


def word2dictionary(word, case):
    dic = set()
    words = set()
    dic.add(word)
    for i in range(0, len(word)):
        words = set(dic)
        for w in words:
            b = ""  # String before letter
            a = ""  # String after letter
            letter = w[i]
            for j in range(0, i):
                b = b + w[j]
            for j in range(i+1, len(w)):
                a = a + w[j]
            if case == "s":
                dic.add(b + changeCase(letter) + a)
            dic.add(b + letterToNumber(letter) + a)
    return dic


if len(sys.argv) < 2:
    print "Missing arguments. -h for help"
else:
    if sys.argv[1] == '-h':
        print """usage: python w2d.py [option] word
Options and arguments available:
-h : display help.
-s : generate dictionary generating lower and uppercase letters.
-i : generate dictionary without generating case changes.

Example:
python w2d.py -s test (81 combinations)
python w2d.py -i test (16 combinations)"""
    elif len(sys.argv) == 3:
        dic = set()
        word = sys.argv[2]
        arg = sys.argv[1]
        if arg == '-i':
            case = "i"
            word = word.lower()
        elif arg == '-s':
            case = "s"
        else:
            print "Wrong argument. -h for help"
            quit()
        dic = word2dictionary(word, case)
        filename = word + ".out"
        with open(filename, "w") as f:
            f.write('\n'.join(dic)+'\n')
        print "Generated " + str(len(dic)) + " combinations. Saved " \
            "in " + filename
    else:
        print 'Missing arguments. -h for help'
