#!/usr/bin/python
import sys
import time

l2n = dict(zip("aAeEiIlLoOsStTgGgB","443311110055776688"))

def letterToNumber(l):
	if l in l2n:
		l=l2n[l]
	return l

def changeCase(l):
	if l.islower():
		l=l.upper()
	else:
		l=l.lower()
	return l

def word2dictionary(word):
	dic=set()
	words=set()
	dic.add(word)
	for i in range(0,len(word)):
		words=set(dic)
		for w in words:
			b="" # string before letter
			a="" # string after letter
			letter=w[i]
			for j in range(0,i):
				b=b+w[j]
			for j in range(i+1,len(w)):
				a=a+w[j]
			dic.add(b+changeCase(letter)+a)
			dic.add(b+letterToNumber(letter)+a)
	return dic

if len(sys.argv) < 2:
	print "Missing word. Syntax: python w2d.py word"
else:
	dic=set()
	word=sys.argv[1]
	dic=word2dictionary(word)
	filename=word+".out"
	with open(filename,"w") as f:
		f.write('\n'.join(dic)+'\n')
	print "Generated "+str(len(dic))+" combinations. Saved in "+filename
