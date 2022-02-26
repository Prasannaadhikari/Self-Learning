import re

#a = 'Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com'

file = open('websiteData.txt','r',encoding='UTF-8')
files = file.readlines()

c={}

for lines in files:
	lines=lines.split(' ')
	for line in lines:
		if re.match(r'[\w\.-]+@[\w\.-]+', line):    	
			if line[-1] =='.':
				line = line.strip('.') 

			if line in c:
				c[line]+=1
			else:
				c[line]=1

for i in c:
	if len(i.split('.'))>2:
		print(i +' Occurance ' + str(c[i]) + ': Human')
	else:
		print(i +' Occurance ' + str(c[i]) + ": Not Human")
