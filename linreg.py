#!/usr/bin/env python2

"""
a = n * sum(x*y)
b = sum(x) * sum(y)
c = n * sum(x^2)
d = sum(x)^2
m = (a - b)/(c - d)
if m > 0 trend = up
else if m < 0 trend = down
"""

import math

data1 = {1:98, 2:100, 3:105, 4:120} #up
data2 = {1:120, 2:103, 3:101, 4:99} #down
data3 = {1:98, 2:100, 3:102, 4:20} #down
data4 = {1:100, 2:99, 3:99, 4:100} #undetermined

def linear_regression(data):

	n = len(data)

	print 'x = %s' % data.keys()
	print 'y = %s' % data.values()
	print 'n = %d' % n

	a = c = 0

	for idx in data:
		a += data[idx] * idx
	a *= n

	b = math.fsum(data.keys()) * sum(data.values())

	for idx in data.keys():
		c += pow(idx,2)
	c *= n 

	d = pow(sum(data.keys()),2)

	m = (a - b) / (c - d)

	if m > 0: print '\nMarket trending upwards\n'
	elif m < 0: print '\nMarket trending downwards\n'
	else: print '\nMarket trend undetermined\n'

	print 'a = %.2f' % a
	print 'b = %.2f' % b
	print 'c = %d' % c
	print 'd = %d' % d
	print 'm = %.2f\n' % m

linear_regression(data1)
linear_regression(data2)
linear_regression(data3)
linear_regression(data4)
