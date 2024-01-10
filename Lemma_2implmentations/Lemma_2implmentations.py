import time
# from prettyprint import *
import re
start = time.time()

# Implmentation 1
def pos(x, L):
    if (len(L) == 0):
        return None
    else:
        if (x == L[0]):
            return 0
        else:
            return (1 + (pos(x, L[1:])))

"""
>>> pos('c', ['a','b','c'])
2
>>> pos('b', ['a','b','d'])
1
>>> pos('a', ['a','b'])
0
"""

def rporec(str1, str2, m, n, i, j, flag, symlist):
    if ((i > m) and (j > n)):
        return flag
    else:
        if (j > n):
            return True
        elif (i > m):
            return False
    x = pos(str1[i], symlist)
    y = pos(str2[j], symlist)
    #print(i, " ", j, " ", x, " ", y);
    if (x < y):
        return rporec(str1, str2, m, n, i, j + 1, flag, symlist)
    elif (x == y):
        return rporec(str1, str2, m, n, i + 1, j + 1, flag, symlist)
    else:
        if (flag):
            return rporec(str1, str2, m, n, i + 1, j, flag, symlist)
        else:
            return rporec(str1, str2, m, n, i + 1, j, True, symlist)

'''print(rporec('ac', 'abbc', 0, 0, 0, 0, False, ['a', 'b','c']))
False
print(rporec('abc', 'abbc', 0, 0, 2, 3, False, ['a', 'b','c']))
False
print(rporec('ab', 'bbbbbbbac', 3, 2, 0, 0, True, ['a', 'b','c']))
True'''

def rpo_original(str1, str2, symlist):
    if (str1 == ''):
        return False
    elif (str2 == ''):
        return True
    m = len(str1) - 1
    n = len(str2) - 1
    return rporec(str1, str2, m, n, 0, 0, False, symlist)

rpoo = rpo_original

'''

>>> rpoo("abba","baab",['a', 'b'])
False
>>> rpoo("abab","baab",['a', 'b'])
True
>>> rpoo('ab', 'bbbbbbbac', ['a', 'b', 'c'])
True
>>> rpoo('a', 'a', ['a', 'b', 'c'])
False
>>> rpoo('a', 'bbbbb', ['a', 'b', 'c'])
True

'''

end = time.time()


print("Implmentation - Process executed in {0} ms".format((end-start)*10**3))


#Implementation 2
start = time.time()
def find_common_suffix(s1, s2):

    suffix = ''
    for i in range(1, min(len(s1), len(s2))+1):
        if s1[-i] == s2[-i]:
            suffix = s1[-i] + suffix
        else:
            break
    return suffix


"""
>>> find_common_suffix('ababab', 'ccabcab')
ab
>>> find_common_suffix('ababab', 'ccabcb')
b
>>> find_common_suffix('ababab', 'ab')
ab
"""
 
def remove_common_suffix(s1, s2):

    suffix = find_common_suffix(s1, s2)
    if (suffix == ''):
        return (s1, s2)
    else:
        return (s1[:-len(suffix)], s2[:-len(suffix)])

"""
>>> remove_common_suffix('ababab', 'ccabcab')
('abab', 'ccabc')
>>> remove_common_suffix('ababab', 'ccabcb')
('ababa', 'ccabc')
>>> remove_common_suffix('ababab', 'ab')
('abab', '')
"""


def ParikhVector(str1, chars):
    l = []
    for x in chars:
        l.append(x)
    for i,x in enumerate(l):
        count = len([y for y in str1 if x ==y ])
        l[i] = count
    return l

"""
>>> ParikhVector('asds',['a','s','d'])
[1, 2, 1]
>>> ParikhVector('ads',['a','s','d'])
[1, 1, 1]
>>> ParikhVector('sds',['a','s','d'])
[0, 2, 1]
"""
         
def rpo(s1, s2, p_list):
    
    if (s1 == s2):
        return False
    elif len(s1)==0 and len(s2)>0:
        return False
    elif len(s1)>0 and len(s2)==0:
        return True
    else:
      s1,s2 = remove_common_suffix(s1,s2)
    c1 = ParikhVector(s1,p_list) 
    c2 = ParikhVector(s2,p_list) 
    for i,x in enumerate(c1):
        if x>0 and c2[i]==0:
            return True
        elif x==0 and c2[i]>0:
            return False
        elif x==c2[i]==0:
            continue
        elif x>c2[i] and c2[i]>0:
            return True
        elif x==c2[i] and c2[i]>0:
                 splitted_str1 = s1.split(p_list[i])
                 splitted_str2 = s2.split(p_list[i])
                 return rpo(splitted_str1[-1], splitted_str2[-1], p_list)
        elif x<c2[i] and x>0:
            return False
        else:
            return False

"""
>>> rpo("a","bbbbb",['a', 'b', 'c'])
True
>>> rpo("a","a",['a', 'b', 'c'])
False
>>> rpo("ab","bbbbbbbac",['a', 'b', 'c'])
True
>>> rpo("abba","baab",['a', 'b'])
False
"""
print(rpo("abba","baab",['a', 'b']))
False

end = time.time()


print("Implementation2 - Process executed in {0} ms".format((end-start)*10**3))
