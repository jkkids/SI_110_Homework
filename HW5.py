import re
f = open('actualDataHomework5.txt', 'r')
print(sum(int(x) for x in re.findall('[0-9]+', f.read())))