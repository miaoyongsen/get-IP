import re

#book = []
fileName = '/Users/amiao/Desktop/wangziliao/ip.txt'
with open(fileName,'r') as f:
    a = f.read()
books = a.split(',')
for i in books:
    if i[0:5] == 'HTTPS':
        with open('/Users/amiao/Desktop/wangziliao/iphttps.txt','a') as fs:
            fs.write(i + ',')

    else:
        with open('/Users/amiao/Desktop/wangziliao/iphttp.txt', 'a') as fp:
            fp.write(i + ',')

fs.close()
fp.close()

#print(books)