import urllib.request


fhand = urllib.request('https://www.facebook.com/login/')

for line in fhand:
 print (line.strip())
