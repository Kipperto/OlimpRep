def p1():
	s = [[int(input()) for _ in range(2)] for _ in range(3)]
	res = 10000000
	for i in range(3):
		for j in ([1, 2, 3] - i):
				for a in [s[i], s[i][::-1]]:
					for b in [s[j], s[j][::-1]]:
						for c in [s[3-i-j], s[3-i-j][::-1]]:
							res = min(res, max(a[0], b[0], c[0]) * (a[1] + b[1] + c[1]), 
										   max(a[0], b[0] + c[0]) * (a[1] + max(b[1], c[1])))
	print(res)
	




def main():
	p1()

if __name__ == '__main__':
	main()