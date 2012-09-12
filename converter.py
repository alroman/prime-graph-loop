''' 
	Read a file with list of primes, output primes per line
'''

def foo(fil):
	f = open(fil, 'r')
	w = open('prime_list.txt', 'w')

	# advance the pointer
	for i in range(4):
		f.readline()

	for line in f:
		# split by ' '
		s = line.split(' ')
		# only save clean info
		for l in s:
			if(len(l.strip())):
				w.write(l + '\n')

	w.close()
	f.close()

if __name__ == "__main__":
    print "[.] Running converter program"
    foo('10000.txt')
