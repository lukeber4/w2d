#!/usr/bin/python
import sys
import time

if len(sys.argv) < 2:
	print "Missing word."
else:

	word=sys.argv[1]

	filename=word+".out"

	dic=set()
	words=set()
	dic.add(word)
	for i in range(0,len(word)):
		words=set(dic)
		for w in words:
			b=""
			a=""
			for j in range(0,i):
				b=b+w[j]
			for j in range(i+1,len(w)):
				a=a+w[j]
			l=w[i]
			if l.islower():
				dic.add(b+l.upper()+a)
			else:
				dic.add(b+l.lower()+a)
			if l is 'a' or l is 'A':
				dic.add(b+str(4)+a)
			else if l is 'e' or l is 'E':
				dic.add(b+str(3)+a)
			else if l is 'i' or l is 'I':
				dic.add(b+str(1)+a)
			else if l is 'l' or l is 'L':
				dic.add(b+str(1)+a)
			else if l is 'o' or l is 'O':
				dic.add(b+str(0)+a)
			else if l is 's' or l is 'S':
				dic.add(b+str(5)+a)
			else if l is 't' or l is 'T':
				dic.add(b+str(7)+a)
			else if l is 'g' or l is 'G':
				dic.add(b+str(6)+a)
				dic.add(b+str(9)+a)
			else if l is 'b' or l is 'B':
				dic.add(b+str(8)+a)	

	with open(filename,"w") as f:
		f.write('\n'.join(dic)+'\n')
		
	print "Generated "+str(len(dic))+" combinations. Saved in "+filename
