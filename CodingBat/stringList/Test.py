def last2(str):
  if len(str) < 2:
    return 0
  last2  = str[len(str)-2:]
  count  = 0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    print(sub)
    if sub == last2:
      count+=1

  return count

#print (last2('hixxhi'))


def array_front9(nums):
    x = False
    for i in range(len(nums)):
        print (i)
        if nums[i] == 9:
            x = True

    return x
#print (array_front9([1, 2, 9, 3, 4]))

def array123(nums):
    x = False
    if len(nums) < 3:
        return x
    else:
        for i in range(len(nums) - 2):
            if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
                x = True
                break
    return x
def string_match(a, b):
  count = 0
  sub_a =[]
  sub_b =[]
  for i in range(len(a)-1):
    sub_a.append(a[i:i+2])
  for i in range(len(b)-1):
    sub_b.append(b[i:i+2])
  shorter = min(len(sub_a),len(sub_b))
  for i in range (shorter):
    if sub_a[i] == sub_b[i]:
        count+=1
  return count


def string_match2(a, b):
    # Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0

    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count = count + 1

    return count
#print (string_match('aabbccdd', 'abbbxxd') )

def extra_end(str):
  return 3*str[-2:]

#print(extra_end('Hi') )
txt = "welcome to the jungle"

x = txt.split()

#print(x)

def date_fashion(you, date):
  ## Check the <=2 case first, since it takes precedence
  ## over the >=8 case.
  if (you <= 2) or (date <= 2):
    return 0
  elif (you >= 8) or (date >= 8):
    return 2
  else:
    return 1

def squirrel_play(temp, is_summer):
  return (not is_summer and 60<=temp<=90)or (is_summer and 60<=temp<=100)
squirrel_play(70, False)

def alarm_clock(day, vacation):
  if not vacation and day!=0 and day!=6:
    return '7:00'
  elif vacation and (day==0 or day ==6 ):
    return 'off'
  else:
    return '10:00'


def make_bricks(small, big, goal):
  if big*5<=goal:
    if (goal-big*5)<=small:
      return True
    else:
      return False
  elif big*5>goal:
    if (big*5) % goal == 0:
      return True
    elif goal%5 <= small:
      return True
    else:
      return False


def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c: sum += a
    if b != a and b != c: sum += b
    if c != a and c != b: sum += c

    return sum

def lucky_sum(a, b, c):
  if a==13: return 0
  elif b==13: return a
  elif c==13: return a+b
  else:
    return a+b+c

#print(lucky_sum(1, 13, 13))


def no_teen_sum(a, b, c):
    sum = 0
    if a == 15 or a == 16:
        sum += a
    if b == 15 or b == 16:
        sum += b
    if c == 15 or c == 16:
        sum += c

    if 13 <= a <= 19 and 13 <= b <= 19 and 13 <= c <= 19:
        return 0 + sum
    elif 13 <= a <= 19 and 13 <= b <= 19:
        return c + sum
    elif 13 <= b <= 19 and 13 <= c <= 19:
        return a + sum
    elif 13 <= c <= 19 and 13 <= a <= 19:
        return b + sum
    elif 13 <= a <= 19:
        return b + c + sum
    elif 13 <= b <= 19:
        return a + c + sum
    elif 13 <= c <= 19:
        return a + b + sum
    else:
        return a + b + c

def close_far(a, b, c):
  close1 = False
  close2 = False
  if abs(a-b) <=1:
    close1 = True
  if abs(a-c)<=1:
    close2 = True
  if abs(b-c) <=1:
    close1 = close2
  return (not close1 and close2) or (not close2 and close1)


def make_chocolate(small, big, goal):
  if big*5<=goal:
    if (goal-big*5)<=small :
      return (goal-big*5)
    else:
      return -1
  elif big*5>goal:
    if (big*5) % goal == 0:
      return 0
    elif goal%5 <= small:
      return  goal%5
    else:
      return -1
def double_char(str):
  x=''
  for i in range (len(str)):
    x+= 2*str[i]
  return x
print(double_char('The'))

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count+=1
  return count

print(count_hi('ABChi hi'))

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'cat':
      cat += 1
    elif str[i:i+3] == 'dog':
      dog +=1
  return cat == dog

print(cat_dog('catdog'))


def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i + 2] == 'co' and str[i+3] == 'e':
            count += 1
    return count

print(count_code('cozexxcope') )


def sum13(nums):
    if len(nums) != 0:
        sum = 0
        flag = 0
        for i in range(len(nums)):
            if nums[i] != 13 and flag != 1:
                sum += nums[i]
                flag = 0
            elif nums[i] == 13:
                flag = 1
            else:
                flag = 0

        return sum
    else:
        return 0


def xyz_there(str):
    result = False
    dot = False
    for i in range(len(str) - 2):
        if i == 0 and str[0:3] == "xyz":
            result = True
            break
        if i >= 1:
            if str[i - 1] == '.':
                dot = True
            else:
                dot = False
            if str[i:i + 3] == 'xyz' and not dot:
                result = True
                break

    return result


print(xyz_there('xyz.abc'))


def sum67(nums):
    if len(nums) != 0:
        sum = 0
        ignore = False
        for i in range(len(nums)):
            if nums[i] != 6 and nums[i] != 7 and not ignore:
                sum += nums[i]
            elif nums[i] == 6:
                ignore = True
            elif nums[i] == 7 and ignore:
                ignore = False
            elif nums[i] == 7 and not ignore:
                sum += nums[i]

        return sum

    else:
        return 0
