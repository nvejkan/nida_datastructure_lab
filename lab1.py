#Speedometer

def speed(s,t):
    return s/t

def BMI(w,h):
    '''
    weight (kg) / [height (m)]2
    '''
    bmi = round(w/(h**2),1)
    if bmi < 18.5:
        print('Underweight')
        return 'Underweight'
    elif bmi >= 18.5 and bmi < 25:
        print('Normal or Healthy Weight')
        return 'Normal or Healthy Weight'
    elif bmi >= 25 and bmi < 30:
        print('Overweight')
        return 'Overweight'
    else:
        print('Obese')
        return 'Obese'

def tip_cal(amount,tip_percent):
    return amount*(tip_percent/100)

def rect_area(w, h):
    return w*h

def high_pass_filter(in_list,cutoff):
    out_list = [ i if i<cutoff else 0 for i in in_list ]
    return out_list

def count(in_list):
    '''
    This will count list len
    '''
    #return len(in_list)
    count = 0
    for i in in_list:
        count = count + 1
    return count

def add(in_list):
    '''
    This will sum list
    '''
    #return sum(in_list)
    sum = 0
    for i in in_list:
        sum = sum + i
    return sum

def mean(in_list):
    #call the above add and count
    return add(in_list)/count(in_list)

def count_vowel(p_str):
    vowel_list = ['a','e','i','o','u']

    return add([ 1 if (i in vowel_list) else 0 for i in p_str])

def sum_sq(n):
    '''
    returns the sum of the squares of all the odd positive integers smaller than n    
    '''

    odd_nums = [ i**2 if i%2 else 0 for i in range(1,n)]
    return add(odd_nums)

def is_num_distinct(p_numlist):
    '''
    takes a sequence of numbers and determines if all the numbers are different from each other
    '''
    set_num = set()
    for i in p_numlist:
        if i not in set_num:
            set_num.add(i)
        else:
            return False

    return True
    

import unittest

class TestStringMethods(unittest.TestCase):

    def test_speed(self):
        self.assertEqual(speed(50,2), 50/2)

    def test_BMI(self):
        self.assertEqual(BMI(60,1.8), 'Normal or Healthy Weight')
        self.assertEqual(BMI(100,1.4), 'Obese')
        #self.assertTrue(BMI(60,1.8))
        #self.assertFalse('Foo'.isupper())
        
    def test_tip(self):
        self.assertEqual(tip_cal(500,10), 50)

    def test_rect_area(self):
        self.assertEqual(rect_area(2, 800), 1600)
        self.assertEqual(rect_area(10.5, 2), 21)
        
    def test_high_pass_filter(self):
        self.assertEqual(high_pass_filter([1,2,3,4,5,6,8,88,100,0,-9,55,10],20), [1, 2, 3, 4, 5, 6, 8, 0, 0, 0, -9, 0, 10])
        self.assertEqual(high_pass_filter([1,2,3],1), [0,0,0])

    def test_mean(self):
        import numpy as np
        self.assertEqual(mean([1,2,3,5,158,99]), np.mean([1,2,3,5,158,99]))

    def test_count_vowel(self):
        self.assertEqual(count_vowel('tongmz bird stupid sharp'), 5)
        self.assertEqual(count_vowel('good cat'), 3)

    def test_sum_sq(self):
        self.assertEqual(sum_sq(2), 1)
        self.assertEqual(sum_sq(5), 10)
        self.assertEqual(sum_sq(10), 165)
    def test_is_num_distinct(self):
        self.assertTrue(is_num_distinct([1,2,3,4,5]))
        self.assertFalse(is_num_distinct([1,2,3,4,5,5]))
        self.assertFalse(is_num_distinct([10,12,13,12,55,59]))
if __name__ == '__main__':
    unittest.main()
