a, b, c = [[int(input()) for _ in range(2)] for _ in range(3)]

def r(a, b, c):
	return min(max(a[0], b[0], c[0]) * (a[1] + b[1] + c[1]), 
			   max(a[0], b[0] + c[0]) * (a[1] + max(b[1], c[1])))
			   
res = 10000000
s = [a, b, c]
for i in range(3):
	for j in range(3):
		if i != j:
			for x in [s[i], s[i][::-1]]:
				for y in [s[j], s[j][::-1]]:
					for z in [s[3-i-j], s[3-i-j][::-1]]:
						res = min(res, r(x, y, z))
		
print(res)