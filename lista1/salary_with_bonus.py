# -*- coding: utf-8 -*-
first_name = input()
salary = float(input())
total_value_sold = float(input())

print('TOTAL = R$ ' + '%0.2f' % (salary + total_value_sold * 0.15))
