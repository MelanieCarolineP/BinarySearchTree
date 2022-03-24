from Binary_Search_Tree import Binary_Search_Tree

class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    if self.__n * other.__d < other.__n * self.__d:
        return True
    return False

  def __gt__(self, other):
      if self.__n * other.__d > other.__n * self.__d:
          return True
  def __eq__(self, other):
    if self.__n * other.__d == other.__n * self.__d:
        return True
    return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)
  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':

  array = [None]*10
  a = Fraction(1,4)
  array[0]= a
  b = Fraction(1,2)
  array[1]= b
  c = Fraction(4,3)
  array[2]= c
  d = Fraction(7,2)
  array[3]= d
  e = Fraction(3,5)
  array[4]= e
  f = Fraction(5,2)
  array[5]= f
  g = Fraction(11,4)
  array[6]= g
  h = Fraction(2,6)
  array[7]= h
  i = Fraction(6,7)
  array[8]= i
  j = Fraction(9,10)
  array[9]= j
  tree = Binary_Search_Tree()
  for item in array:
      tree.insert_element(item)
  print('Original: ' + str(array))
  print('Sorted: ' + str(tree.to_list()))
