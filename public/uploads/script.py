# coding: utf-8

a = input('a = ')
a = int(a)

b = input('b = ') 
b = int(b)

print('\n')

if b > a:
	i = 1 # ����� ������� �����
	j = 1 # ������� �����
	square = 0 # ������� �������� �����
	for i in range(b + 1):
		# ������ ����������� ��������� ������� � ����� �
		if i >= a:
			print(str(i) + 'squared' + '= ' + square)		
		square += j # ������� ���������� ������������ �����
		j += 2 # ��������� ������� �����
elif a <= 0:
	print('a must be greater than 0')
elif b <= 0:
	print('b must be greater than 0')
else:
	print('b must be greater than a')
