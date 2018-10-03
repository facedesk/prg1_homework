from sys import getsizeof

a=2
'''
1gb = 1024 mb
2^10
1mb = 1024 kb
2^10
1kb = 1024 B
2^10
1B = 8 B
2^4
'''
b = (2**4)
kb= (2**10)
mb = kb
gb = mb

ans = b * kb * mb * gb
print(2**ans)
