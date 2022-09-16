# 2588
# a = int(input("숫자1: "))
# b = input("숫자2: ")
#
# c = a*int(b[2])
# d = a*int(b[1])
# e = a*int(b[0])
#
# print(c,d,e,a*int(b[:]), end='=')

# 1330
# a = int(input("숫자1:"))
# b = int(input("숫자2:"))
#
# if a < b:
#     print("<")
# elif a > b:
#     print(">")
# else:
#     print("==")

# # 9498
# point = int(input("시험성적: "))
#
# if 90<=point<=100:
#     print("A")
# elif 80<=point<=89:
#     print("B")
# elif 70<=point<=79:
#     print("C")
# elif 60<=point<=69:
#     print("D")
# else:
#     print("F")

# 2753
# year = int(input("년도: "))
#
# if year % 4 == 0 and year % 400 == 0:
#     print("1")
# elif year % 4 == 0 and year % 100 != 0:
#     print("1")
# else:
#     print("0")

# 14681
# quadrant_x = int(input("x좌표: "))
# quadrant_y = int(input("y좌표: "))
#
# if quadrant_x > 0 and quadrant_y > 0:
#     print("1")
# elif quadrant_x < 0 and quadrant_y > 0:
#     print("2")
# elif quadrant_x < 0 and quadrant_y < 0:
#     print("3")
# else:
#     print("4")

# 2884
# h, m = map(int, input(" ").split())
# m -= 45
# if m < 0:
#     m += 60
#     h -= 1
#     if h < 0:
#         h = 23
# print(h, m)

# 2739
# n = int(input("숫자를 입력하시오: "))
# for i in range(1,10):
#     print(n, '*', i, '=', n*i)

# 10950
# t = int(input())
#
# for i in range(t):
#     a,b = map(int, input().split())
#     print(a+b)

# 8393
# n = int(input())
# sum = 0
#
# for i in range(n+1):
#     sum += i
# print(sum)

# 15552
# import sys
#
# t = int(input())
# for i in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 2741
# n = int(input())
#
# for i in range(1, n+1):
#     print(i)

# 2742
# n = int(input())
#
# for i in range(n):
#     print(n-i)

# 11021
# n = int(input())
#
# for i in range(n):
#     a,b = map(int, input().split())
#     print("Case #%d: %d"%(i+1,a+b))

# 11022
# n = int(input())
#
# for i in range(n):
#     a,b = map(int, input().split())
#     print("Case #%d: %d + %d = %d"%(i+1,a,b,a+b))

# 2438
# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)

# 2439
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

# 10871
# n,x = map(int, input().split())
# a = list(map(int, input().split()))
#
# for i in range(n):
#     if a[i] < x:
#         print(a[i], end=" ")

# 10952
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# 10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# 1110
# n = int(input())
# num = n
# cnt = 0
#
# while True:
#     a = num // 10
#     b = num % 10
#     c = (a+b) % 10
#     num = (b*10) + c
#
#     cnt = cnt + 1
#     if num == n:
#         break
# print(cnt)

# 10818
# n = int(input())
# num = list(map(int, input().split()))
# print(min(num),max(num))

# 2562
# num = []
# for i in range(9):
#     num.append((int(input())))
# print(max(num))
# print(num.index(max(num))+1)

# 2577
# A = int(input())
# B = int(input())
# C = int(input())
#
# D = list(str(A * B * C))
#
# for i in range(10):
#     print(D.count(str(i)))

# 3052
# num = []
# for i in range(10):
#     n = int(input())
#     num.append(n % 42)
# num = set(num)
# print(len(num))

# 1546
# n = int(input())
# test_list = list(map(int, input().split()))
# max_score = max(test_list)
#
# new_list = []
# for score in test_list:
#     new_list.append(score/max_score * 100)
# test_avg = sum(new_list) / n
# print(test_avg)

# 8958
# n = int(input())
#
# for i in range(n):
#     a = input()
#     score = 0
#     sum_score = 0
#     for j in a:
#         if j == 'o':
#             score += 1
#         else:
#             score = 0
#         sum_score += score
#     print(sum_score)

# 10773
# k = int(input())
#
# stack = []
#
# for i in range(k):
#     a = int(input())
#     if a == 0:
#         stack.pop()
#     else:
#         stack.append(a)
# print(sum(stack))

# 11399
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# cnt = 0
# s = 0
# for i in range(n):
#     cnt += data[i]
#     s += cnt
# print(s)
