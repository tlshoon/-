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

# 샤틀버스
# x,y= input().split()
# x = int(x)
# y = int(y)
#
# if x>y:
#     print(x+y)
# else:
#     a = y//x
#     b = a*x
#     print(y-b)

# 2606번
# from collections import deque
# n = int(input())  # 컴퓨터 개수
# v = int(input())  # 연결선 개수
#
# graph = [[] for _ in range(n+1)]  # 그래프 초기화
# visited = [0] * (n+1)  # 방문한 컴퓨터인지 표시
#
# for i in range(v):
#     a,b = map(int,input().split())
#     graph[a] += [b]  # a에 b연결
#     graph[b] += [a]  # b에 a연결  -> 양방향  // 이중리스트
#
# visited[1] = 1  # 1번부터 컴퓨터 시작이니 방문 표시
# q=deque([1])
#
# while q:
#     start = q.popleft()
#     for nx in graph[start]:
#         if visited[nx] == 0:시
#             visited[nx] = 1
#
# print(sum(visited)-1)

# 1260번
# from collections import deque
# n, m, v = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
#
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a] += [b]
#     graph[b] += [a]
#
# for i in range(m):
#     graph[i].sort()
#
#
# visited_bfs = [False] * (n+1)
# visited_dfs = [False] * (n+1)
#
# def dfs(graph, start, visited_dfs):
#     visited_dfs[start] = True
#     print(start,end=' ')
#     for i in graph[start]:
#         if visited_dfs[i] == False:
#             dfs(graph,i,visited_dfs)
#
# def bfs(graph, start, visited_bfs):
#     queue=deque([start])
#     visited_bfs[start] = True
#     while queue:
#         bfs_now = queue.popleft()
#         print(bfs_now,end=' ')
#         for i in graph[bfs_now]:
#             if visited_bfs[i] == False:
#                 queue.append(i)
#                 visited_bfs[i] = True
#
# dfs(graph,v,visited_dfs)
# print(sep='')
# bfs(graph, v, visited_bfs)

# 14716번
# n,m = map(int,input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))
#
#
# def dfs(x,y):
#     if x<= -1 or x >=n or y <= -1 or y >=m:
#         return False
#     if data[x][y] == 1:
#         data[x][y] = 0
#         dfs(x-1,y)
#         dfs(x, y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         dfs(x+1, y+1)
#         dfs(x-1, y+1)
#         dfs(x+1, y-1)
#         dfs(x-1, y-1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1
# print(result)

# 11047번
## 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구합니다.
# N, K = map(int, input().split()) # N : 화폐 종류수, K : 거슬러 줄 돈
#
# # 2. 계산대에 있는 화폐들을 리스트의 형태로 입력받습니다.
# coins = []
# for _ in range(N):
#     coins.append(int(input()))
# coins.sort(reverse=True)
# # coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
#
# # 3. 만약 '계산대 안에 있는 화폐'보다 '거슬러 줄 돈'이 크다면
# # 돈을 거슬러 줍니다.
# answer = 0
# for coin in coins:
#     if K >= coin:
#         answer += K // coin  # 몫만큼 더하기
#         K %= coin # 나머지 할당
#         if K <= 0: # 만약 K가 0이면 반복문을 탈출합니다.
#        		break
# print(answer) # 거슬러 준 동전 + 화폐의 수

# 1026번
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
#
# a.sort()
# b.sort(reverse=True)
# s = 0
# for i in range(n):
#     s += a[i] * b[i]
# print(s)

# 4963번
# def bfs(x,y):
#     if 0<= x and x < h and 0 <= y and y < w:
#         if graph[x][y] == 1:
#             graph[x][y] = 2
#             bfs(x-1,y-1)
#             bfs(x-1,y)
#             bfs(x-1,y+1)
#             bfs(x,y+1)
#             bfs(x,y-1)
#             bfs(x+1,y-1)
#             bfs(x+1,y)
#             bfs(x+1,y+1)
#             return True
#         return False
#
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]
#
# while True:
#     w, h = map(int, input().split())
#     if not w and not h:
#         break
#     graph = [list(map(int,input().split())) for _ in range(h)]
#     cnt = 0
#
#     for i in range(w):
#         for j in range(h):
#             if bfs(i,j) == True:
#                 cnt += 1
#     print(cnt)

# 1427번
# n = list(map(int,input()))
# n.sort(reverse=True)
# for i in n:
#     print(i,end='')

# 11656번
# s = input()
#
# dict = []
# for i in range(len(s)):
#     dict.append(s[i:])
#
# dict.sort()
#
# for i in dict:
#     print(i,sep='')

# 9237번
# n = int(input())
# t = list(map(int,input().split()))
# t.sort(reverse=True)
#
# for i in range(n):
#     t[i] = t[i] - (n-1-i)
#
# max_value = max(t)
# cnt = n + 1 + max_value
#
# print(cnt)

