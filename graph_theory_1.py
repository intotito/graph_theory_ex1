import math
import math

def sumMultiply(a: int, b: int) -> int:
    # Calculates the product of two integer numbers.
    # This method is evaluated using only sum and subtraction operations.
    num1 = max(a, b) if ((a < 0) ^ (b < 0))  else abs(a)
    num2 = min(a, b) if ((a < 0) ^ (b < 0)) else abs(b)
    ans = 0
    for i in range(num1):
        ans += num2
    return ans

print(sumMultiply(-5,-0))

def isPalindrome(text: str) -> bool:
    # Checks if a string is a palindrome.
    m_text = text.replace(" ", "")
    for i in range(len(m_text) // 2):
        if (not (m_text[i].lower() == m_text[len(m_text) - i - 1].lower())):
            return False
    return True

print(isPalindrome("Otito"))

def simpleInterest(prcpl: int, rate: int, period: int) -> float:
    # Calculates due payment for a loan with simple interest over a period
    return prcpl + prcpl * rate * period / 100

print(simpleInterest(1000, 7, 10))

def compoundInterest(prcpl: int, rate: int, period: int) -> float:
    # Calculates due payment for a loan with a compound interest over a period
    m_prcpl = prcpl
    for i in range(period):
        m_prcpl += (m_prcpl * rate / 100)
    return m_prcpl

print(compoundInterest(1000, 7, 10))

def newtonsRoot(num: int) -> float:
    # Calculates the square root of an number using Newtons Root method
    ran = num / 4
    while True:
        print('Random', ran)
        ran = ran - (ran ** 2 - num) / (2 * ran)
        if(round(ran ** 2, 6) == num):
            return round(ran, 6)

print(newtonsRoot(144))

def pitondecs(rnd : int) -> float:
    # Rounds the value of PI to the supplied decimal places
    return round(math.pi, rnd)


print(pitondecs(6))

def etondecs(num: int) -> float:
    return round(math.exp(1), num)

print(etondecs(6))

def caesar(text: str, shift: int) -> str:
    m_str = []
    for i in range (len(text)):
        if(ord(text[i]) <= ord('z') and ord(text[i]) >= ord('A')):
            m_str.append(chr(ord(text[i]) + shift))
        else: 
            m_str.append(text[i])
    return ''.join(m_str)

print(caesar('Hello, world!', 2))

def sortList(list: list) -> list:
    # Sorts the supplied list argument
    # Implemented using a make-shift quick sort
    length = len(list)
    contnue = True
    count = 0
    while contnue:
        pivot = list[length - 1]
        contnue = False
        for i in range(len(list) - 1):
            count += 1
            temp_ith = list[i]
            if(list[i] > list[i + 1]):
                list[i] = list[i + 1]
                list[i + 1] = temp_ith
                contnue = True
            else: 
                if (list[i] > pivot):
                    list[i] = pivot
                    list[length - 1] = temp_ith
                    pivot = temp_ith
                    contnue = True
    print('count', count)
    return list

print(sortList([3, 7, 8, 5, 2, 1, 9, 5, 4]))
    
def countString(string: str) -> str:
    set = {}
    for i in len(str):
        if(string[i] in set):
            temp = set.get
        else : 
            set.add(0)


count = [0]
def quickSort(list: list, start: int, stop: int, count) -> list:
    i_pivot = stop
    pivot = list[i_pivot]
    i = start
    while(i < i_pivot):
        count[0] += 1
        temp = list[i]
   #     print('count = ', count[0])

    #    print('XXXXXX', 'i=', i, 'list[i]=', list[i])
        if(list[i] > pivot):
      #      print('i=', i, 'i_pivot=', i_pivot, 'pivot=', pivot, 'list[i]=', list[i])
            list[i] = list[i_pivot - 1]
            list[i_pivot] = temp
            i_pivot -= 1
            list[i_pivot] = pivot
        else:
            i += 1
       #     print('increment at', i)
    if((i_pivot - 1) - start > 0):
        quickSort(list, start, i_pivot - 1, count)
    if(stop - (i_pivot + 1) > 0):
        quickSort(list, i_pivot + 1, stop, count)
 #   print('Count =', count, 'i_pivot=', i_pivot, 'i=', i)
    return list

list =[2, 43, 52, -4, -5, 34, 8, 23, 14, 16, 4, 3, 1, -5, 0, 20]
print(quickSort(list, 0, len(list) - 1, count))
print('count = ', count[0])
