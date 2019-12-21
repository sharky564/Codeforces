a=input().split()
m=int(a[0])
s=int(a[1])

def max(m,s):
	if s>9*m:
		return '-1'
	elif s==0 and m==1:
		return '0'
	elif s==0 and m>1:
		return '-1'
	else:
		digits=[]
		while s>=9:
			digits.append('9')
			s-=9
			m-=1
		else:
			while m>0:
				digits.append(str(s))
				s=0
				m-=1
			else:
				return ''.join(digits)

def min(m,s):
	if s>9*m:
		return '-1'
	elif s==0 and m==1:
		return '0'
	elif s==0 and m>1:
		return '-1'
	elif m==1:
		return str(s)
	else:
		digits=[]
		while s>9:
			digits.append('9')
			s-=9
			m-=1
		else:
			while m>1:
				if s>0:
					digits.append(str(s-1))
					s=0
					m-=1
				else:
					digits.append(str(s))
					m-=1
			else:
				if digits[-1]=='9':
					digits.append(str(s))
					return ''.join(digits[::-1])
				else:
					digits.append(str('1'))
					return ''.join(digits[::-1])

print(min(m,s), max(m,s))
