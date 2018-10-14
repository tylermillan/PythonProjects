import sys


nl = int(sys.stdin.readline())
	
for i in range(nl):
	x,y = sys.stdin.readline().strip().split()
	m = int(x)+int(y)
	n = int(x)*int(y)
	sys.stdout.write(str(m)+" "+str(n)+"\n")
