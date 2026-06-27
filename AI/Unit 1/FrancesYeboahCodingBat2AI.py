# $=$^^$=^^=====1=^$^^^1^$^==1 (first time 89.87)
# $^$^^$$^^=====1=^$^^^1^$^==1 (second time 91.6)
# $$$^^$$^^^^===1=^$^^^1^$^==1 (third time 92.49)
# Warm Up 2:

#$
def string_times(str, n):
  return str * n

#$
def front_times(str, n):
  return str[:3] * n

#$
def string_bits(str):
  return str[::2]

#^
def string_splosion(str):
  return "".join(str[:x] for x in range(len(str) + 1))

#^
def last2(str):
  return sum(str[x:x+2] == str[-2:] for x in range(len(str)-2))

#$
def array_count9(nums):
  return nums.count(9)

#$
def array_front9(nums):
  return 9 in nums[:4]

#^
def array123(nums):
  return any(nums[x:x+3] == [1,2,3] for x in range(len(nums)))

#^
def string_match(a, b):
  return sum(a[x:x+2] == b[x:x+2] for x in range(len(a)-1))

# Logic 2:

#=
def make_bricks(small, big, goal):
  return big * 5 + small >= goal and goal % 5 <= small

#=
def lone_sum(a, b, c):
  return sum(x for x in [a,b,c] if [a,b,c].count(x) == 1)

#=
def lucky_sum(a, b, c):
  return 0 if a == 13 else a if b == 13 else a + b if c == 13 else a + b + c

#=
def no_teen_sum(a, b, c):
  return sum(0 if [a,b,c][x] in [13,14,17,18,19] else [a,b,c][x] for x in range(3))

#=
def round_sum(a, b, c):
  return sum(([a,b,c][x] + 10) - ([a,b,c][x] % 10) if [a,b,c][x] % 10 >= 5 else ([a,b,c][x] - [a,b,c][x] % 10) for x in range(len([a,b,c])))

#1
def close_far(a, b, c):
  return (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or (abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2)

#=
def make_chocolate(small, big, goal):
  return -1 if ((big * 5) + small < goal) or (small < goal % 5) else goal - (big * 5) if big * 5 < goal else goal - ((goal // 5) * 5)

# String 2:

#^
def double_char(str):
  return "".join([let * 2 for let in str])

#$
def count_hi(str):
  return str.count('hi')

#^
def cat_dog(str):
  return str.count("cat")==str.count("dog")

#^
def count_code(str):
  return sum([str[x:x+2]=="co" and str[x+3]=="e"  for x in range(len(str)-3)])

#^
def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

#1
def xyz_there(str):
  return any([str[x:x+3] == "xyz" and (x > 0 and str[x-1] != "." or x == 0) for x in range(len(str))])

# List 2:

#^
def count_evens(nums):
  return sum(x % 2 == 0 for x in nums)

#$
def big_diff(nums):
  return max(nums) - min(nums)

#^
def centered_average(nums):
  return (sum(nums) - (max(nums) + min(nums)))//(len(nums)-2)

#=
def sum13(nums):
  return sum(0 if nums[x] == 13 or (x>0 and nums[x-1] == 13) else nums[x] for x in range(len(nums)))

#=
def sum67(nums):
  return sum([x for i, x in enumerate(nums) if (((nums[(i - nums[i::-1].index(6)):].index(7) + (i - nums[i::-1].index(6))) < i) if (6 in nums[:i+1]) else nums[i])])

#1
def has22(nums):
  return any(nums[x:x+2] == [2,2] for x in range(len(nums)))

# Frances Yeboah - Period 5 - 2027
