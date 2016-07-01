#Author: Abhinav Khare
#Date: 30-06-2016
#Written in 53 Church St, Harvard University ,Cambridge, MA,USA 02138
#this program generates all the possible anagrams of various words in the dictionary i.e. words.txt
import time
start = time.time()
f = open("words.txt")
f = f.read().split()
d = {}
for a in f:
	#hello ehllo
	b=list(a)
	b.sort()
	b="".join(b)  #ehllo   #olleh
	try:
		d[b].append(a)
	except:
		d[b]=[a] #d[ehllo]=hello olleh
for i in d:
	if(len(d[i])>1):
		print(d[i] ,str(len(d[i])) , " anagrams")
end = time.time()
print(end-start)

