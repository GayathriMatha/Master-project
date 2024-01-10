import time

#from prettyprint import *

import re

start = time.time()

def find_common_prefix(s1, s2):

    prefix = ''
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += s1[i]
        else:
            break
    return prefix

"""
>>> find_common_prefix('asd','aqwq')
a
>>> find_common_prefix('aabaabaa','aabacaa')
aaba
>>> find_common_prefix('ab','a')
a
>>> find_common_prefix('abcd','abef')
ab

"""

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

def remove_common_prefix(s1, s2):
 
    prefix = find_common_prefix(s1, s2)
    return (s1[len(prefix):], s2[len(prefix):])

"""
>>> remove_common_prefix('asd','aqwq')
('sd','qwq')
>>> remove_common_prefix('aabaabaa','aabacaa')
('abaa','caa')
>>> remove_common_prefix('ab','a')
('b','')
>>> remove_common_prefix('abcd','abef')
('cd','ef')

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

"""
print("Process executed in {0} s".format(round((end-start),1)))
"""

rcs = remove_common_suffix

end = time.time()

def is_subseq(x, y):  # Stephan Pochmann on the internet
    it = iter(y)
    return all(c in it for c in x)

"""
>>> is_subseq('ac', 'abc')
True
>>> is_subseq('ac', 'abbc')
True
>>> is_subseq('ac', 'bbbbabbc')
True
>>> is_subseq('ac', 'bbbbcab')
False
>>> is_subseq('', 'ac')
"""

def tail(ls):
    if (len(ls) == 0):
        return None
    else:
        return ls[1:]
    
"""
>>> tail(['a','d','as'])
['d', 'as']
>>> tail(['aa','ad','aass'])
['ad', 'aass']

"""

def higher_prec(sym1, sym2, prec_list):
    sym = hd(prec_list)
    if (sym1 == sym):
        return True
    elif (sym2 == sym):
        return False
    else:
        return higher_prec(sym1, sym2, tail(prec_list))

"""
>>> higher_prec('b', 'd', pls)
True
>>> higher_prec('b', 'a', pls)
False
>>> higher_prec('d', 'a', pls)
False
"""

def decompose(str, symbol):
    w = re.split(symbol, str)
    return w

"""
>>> decompose('babbaba', 'a')
['b', 'bb', 'b', '']
>>> decompose('babbabccac', 'a')
['b', 'bb', 'bcc', 'c']
>>> decompose('babbaba', 'b')
['', 'a', '', 'a', 'a']
"""
def explode(str):
    return list(str)

'''
>>> explode('ads')
['a', 'd', 's']
>>> explode('qwq')
['q', 'w', 'q']

'''

def hd(L):
    if type(L) == type([]):
        if len(L) == 0: return None
        else: return L[0]
    else: return None
"""
>>> hd(['ad','a'])
ad
>>> hd(['','a'])

>>> hd(['a','aasa'])
a
"""

def rpoeq(str1, str2, preclist):
    (str1, str2) = remove_common_suffix(str1, str2)
    if (str1 == str2):
        return True
    else:
        if is_subseq(str1, str2):
            return False
        else:
            if is_subseq(str2, str1):
                return True
            else:
                xa = str1[0]
                xb = str2[0]
                if (xa == xb):
                    return rpoeq(str1[1:], str2[1:], preclist)
                else:
                    if higher_prec(xa, xb, preclist):
                        return rpoeq(str1, str2[1:], preclist)
                    else:
                        return rpoeq(str1[1:], str2, preclist)

"""
>>> rpoeq('abc', 'abb', ['a', 'b', 'c'])
False
>>> rpoeq('abc', 'bbbbbac', ['a', 'b', 'c'])
True
>>> rpoeq('abc', 'bbbbbacccc', ['a', 'b', 'c'])
True
"""

def rpo(str1, str2, preclist):
    if (str1 == str2):
        return False
    else:
        return rpoeq(str1, str2, preclist)

"""
>>> rpo('a', 'bbbbb', ['a', 'b', 'c'])
True
>>> rpo('a', 'a', ['a', 'b', 'c'])
False
>>> rpo('ab', 'bbbbbbbac', ['a', 'b', 'c'])
True
>>> rpo('abba', 'baab', ['a', 'b'])
False
"""
end = time.time()


print("Process executed in {0} ms".format((end-start)*10**3))

