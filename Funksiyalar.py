def Tup(num):
	for x in range(2,num):     
        if num%x == 0:
	        return False
    return True
	

a = 15
if Tub(a):
   print('tub son ekan')
else:
	print('tobson emas ekan')

