# -*- coding: utf-8 -*-
__author__ = 'zhangsheng'

import random
import itertools


def GenerateData():
	random.seed(1)
	n = 100
	unknown = 10
	seq = list(range(1,n+1))
	random.shuffle(seq)

	unknown_pos = random.sample(range(1,n+1), unknown)
	unknown_seq = [seq[i] for i in unknown_pos]

	order_count = 0
	for i in range(n-1):
		for j in range(i+1,n):
			if seq[i] < seq[j]:
				order_count += 1

	for i in unknown_pos:
		seq[i] = 0

	with open('./data1.txt', 'w') as f:
		print('%d %d' % (n, order_count), file=f)
		print(' '.join(map(str, seq)), file=f)
		print(' '.join(map(str, unknown_pos)), file=f)
		print(' '.join(map(str, unknown_seq)), file=f)
		print(dict(zip(unknown_pos,unknown_seq)),file=f)


def Solve():
	result = 0
	with open('./data1.txt') as f:
		n, k = list(map(int, f.readline().strip().split()))
		seq = list(map(int, f.readline().strip().split()))

	unknown_pos = [i for i in range(n) if seq[i] == 0]

	unknown_seq = list(set(list(range(1,n+1))) - set(seq))

	print(n)
	print(k)



	unknown_pos = sorted(unknown_pos)
	print(unknown_pos)
	print(unknown_seq)

	order_count = 0
	for i in range(n-1):
		if seq[i] == 0:
			continue
		for j in range(i+1,n):
			if seq[j] == 0:
				continue
			if seq[i] < seq[j]:
				order_count += 1

	print(order_count)
	print(seq)
	# rand_order = 0

	flag = 0
	for rand_seq in itertools.permutations(unknown_seq):
		# rand_seq = [66, 92, 59, 24, 89, 29, 99, 2, 70, 18]
		# print(rand_seq)
		# break
		flag += 1
		if flag == 1000000:
			print('1000000')
		if flag == 2000000:
			print('2000000')
		if flag == 3000000:
			print('3000000')

		rand_order = 0
		for i in range(len(unknown_pos)):
			# print(unknown_pos[i])
			for j in range(unknown_pos[i]):
				if seq[j] !=0 and seq[j] < rand_seq[i]:
					rand_order += 1
			for j in range(unknown_pos[i]+1,n):
				if seq[j] != 0 and seq[j] > rand_seq[i]:
					rand_order += 1
		for i in range(len(unknown_pos)-1):
			for j in range(i+1,len(unknown_pos)):
				if rand_seq[i] < rand_seq[j]:
					rand_order += 1
		if rand_order + order_count == k:
			result += 1
		# print(rand_order)
		# break
	#
	# rand_seq = [66, 92, 59, 24, 89, 29, 99, 2, 70, 18]
	# for i in range(len(unknown_pos)):
	# 	assert seq[unknown_pos[i]] == 0
	# 	seq[unknown_pos[i]] = rand_seq[i]
	#
	# cc = 0
	# for i in range(len(unknown_pos)):
	# 	for j in range(unknown_pos[i]):
	# 		if seq[j] < rand_seq[i]:
	# 			cc += 1
	# 	for j in range(unknown_pos[i]+1,n):
	# 		if seq[j] > rand_seq[i]:
	# 			cc += 1
	# 	print(cc)



	return result




if __name__ == '__main__':
	# GenerateData()
	print(Solve())