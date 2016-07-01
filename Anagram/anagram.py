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
#pprint.pprint(d)
#print(f)
'''
for a in f:
	l=[a]
	for b in f:
		if(anagram(a,b)):
			l.append(b)
	#print(l)
end = time.time()
print(end-start)
#print(anagram(input(),input()))
'''
