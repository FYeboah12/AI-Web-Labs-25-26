# Warm Up 1:

def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or not (a_smile or b_smile)

def sum_double(a, b):
  return 2 * (a + b) if a == b else a + b

def diff21(n):
  return 2 * abs(21 - n) if n > 21 else 21 - n

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
  return (negative and (a < 0 and b < 0)) or (not negative and ((a < 0 and b > 0) or (a > 0 and b < 0)))

# String 1:
def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

def make_out_word(out, word):
  return out[0:len(out)//2] + word + out[len(out)//2:]

def extra_end(str):
  return str[len(str)-2:] * 3

def first_two(str):
  return str if len(str) < 2 else str[0:2]

def first_half(str):
  return str[:len(str)//2]

def without_end(str):
  return str[1:len(str)-1]

# List 1:
def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums)-1]

def make_pi(n):
  return [int(digit) for digit in "31415926535897932384626433"[:n]]
#return [3,1,4]

def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]

def sum3(nums):
  return sum(nums) 
# return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  return nums[1:len(nums)] + [nums[0]] if len(nums) > 1 else nums 
# return [nums[1], nums[2], nums[0]]
  
def reverse3(nums):
  return nums[::-1] 
  #return [nums[2], nums[1], nums[0]]
def max_end3(nums):
  return [nums[0]]*len(nums) if nums[0] > nums[len(nums)-1] else [nums[len(nums)-1]]*len(nums) 
#return [nums[0],nums[0],nums[0]] if nums[0] > nums[len(nums)-1] else [nums[len(nums)-1],nums[len(nums)-1],nums[len(nums)-1]] 

# Logic 1:

def cigar_party(cigars, is_weekend):
  return is_weekend and cigars >= 40 or cigars >= 40 and cigars <= 60

def date_fashion(you, date):
  return 0 if (you <= 2 or date <= 2) else 2 if (you >= 8 or date >= 8) else 1

def squirrel_play(temp, is_summer):
  return is_summer and temp >= 60 and temp <= 100 or temp >= 60 and temp <= 90

def caught_speeding(speed, is_birthday):
  return 2 if (is_birthday and speed >= 86) or (not is_birthday and speed >= 81) else 1 if (is_birthday and speed >= 66 and speed <= 85) or (not is_birthday and speed >= 61 and speed <= 80) else 0

def sorta_sum(a, b):
  return 20 if a + b >= 10 and a + b <= 19 else a + b

def alarm_clock(day, vacation):
  return "10:00" if (not vacation and (day == 0 or day == 6)) or (vacation and day != 0 and day != 6) else "7:00" if not vacation else "off"

def love6(a, b):
  return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
  return (outside_mode and (n <= 1 or n >= 10)) or (not outside_mode and n >= 1 and n <= 10)

# Frances Yeboah, Period 5, 2027