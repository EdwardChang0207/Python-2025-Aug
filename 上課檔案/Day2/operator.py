#Operator 運算子
#Operatee 運算元

# 1 + 1

'''
1.數學運算子 num op num -> num
+, -, *, /
**(指數、次方)
    2的3次方 = 2 * 2 * 2
    print(2**3)
%(餘數), //(商數)
    20/6 = 3(商數)...2(餘數)
    print(20%6)
    print(20//6)
/(除法) -> float
print(10/2)

2.關係運算子 num op num -> bool
>, <, >=, <=
==(相等), !=(不相等)
print(2>1)
print('a'=='A')
print(2 == 2.0)

3.邏輯運算子 bool op bool -> bool
    邏輯閘 Logic gates
(1)not 反閘
    周杰倫：哎呦不錯喔
    不錯 -> True
    not False -> True
    錯 -> False
    不行 -> False
    not True -> False
    行 -> True
    not True -> False
    print(not True)
    print(not False)
(2)or 或閘
    math or english -> 3000
    T.      F.         T
    F.      T.         T
    T.      T.         T
    F.      F.         F
    (真值表)
    a, b = False, False
    print(a or b)
(3)and 且閘
    hw and 打掃 -> :)
    T.     F.      F
    F.     T.      F
    T.     T.      T 
    F.     F.      F
(4)xor (excursive or) 斥或閘
    珍奶 xor 烏龍拿鐵 -> :)
    T.       F.        T
    F.       T.        T
    T.       T.        F
    F.       F.        F
    [1] not or and
    [2] binary

(1)int
(2)float
(3)String
(4)bool
print(2 + 8 and True)
''' 
# 有/沒有
a, b = 3, 0
print(a ^ b)
print((a or b) and not(a and b))
#white.                 black