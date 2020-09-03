a = [1,2,3,4]
b = 5

try:
	_ = (e for e in b)
except TypeError:
	print('object is not iterable')

print(b)