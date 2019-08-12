## 문자열(String)

(문자열 암호화/압축 = 심화)

- 문자열

  ```
  ##Ascill 
  print(ord('A')) 알파벳 -> Ascii
  print(chr(65))  Ascii -> 알파벳
  
  for i in range(65, 65+26):
  print(chr(i), end=" ")
    -> A-Z 나열
  
  ##유니코드
  전 세계에서 사용할 통일된 코드를 만듬
  
  ##문자열 정렬 = 사전순 정렬
  'aaa' < 'aab'
  'abcd'< 'x' == 문자열 길이와는 상관없다
  ```

- 패턴 매칭

```
긴 문자열    == text    길이 = n    t[i]
짧은 문자열  == pattern  길이 = m   p[j]

모든 패턴매칭 알고리즘 
1) t[i] == p[j]   -> i j 를 1씩 증가하면서 자리를 비교하면 되는 쉬운 유형
2) t[i] != p[j]   -> != 이후에 어떻게 어떻게 알고리즘을 작성해서 문제를 해결할지가 관건.
```

```
kmp 알고리즘 접두어/접미어 
-> 불일치가 발생했을 때 i는 가만히 있고, j = index[0]으로 두고 i의 접미어를 j의 접두어와 비교하면서 나가는게 중복없이 효율적. 이미 앞에서 일치여부를 확인한 부분은 다시 확인할 필요가 없으므로 고지식한 알고리즘보다 효율적 즉, p138 처럼 패턴의 각 위치에 대해 매칭에 실패했을 때 돌아갈 곳을 준비해둔다.

'abcd' 길이=4
		접미어		접두어	
길이 1 	a		d
길이 2	ab		cd	
길이 3	abc		bcd
길이 4	abcd	abcd

전처리: 공통되는 접미어와 접두어를 파악하고 있으면 그 인덱스로 설정하고, 공통되는 부분이 없으면 처음으로 보냄(i= 제자리 , j=index[0]부터 다시 비교) 
```

```
보이어-무어 알고리즘
왼쪽 <- 오른쪽 으로 검색, 뒤에서부터 비교하는게 더 빠른 경우가 많아서 시행
불일치가 발생했을 때, '다음은 어느 부분부터 비교를 해야 의미가 있는지를 탐구'
```



- 재귀호출

  ```python
  재귀적 정의(점화식)을 구현하기 위해서 사용 / 그래프의 깊이 우선 탐색, 백트래킹 등에도 사용됨
  
  **for, while 사용하지 않고 '반복 작업'을 할 수 있다.
  
  # case 1
  def printHello():
      if i < 3:
      	print('Hello!!!')
      	printHello( i + 1)
          
  printHello(0)            #호출
  
  ==
  for i in range(3):
      print('Hello!!!')
  
  # case 2
  def printHello():
      if i == 3:
          print('-------------')
      else:
      	print('Hello!!!')
      	printHello(i + 1)
          
  printHello(0)
  
  # case 3 -> 특정 상수가 아닌 변수 n으로 재귀함수를 제어
  def printHello(i, n):
      if i == n:
          print('-------------')
      else:
      	print('Hello!!!')
      	printHello(i + 1, n)
          
  printHello(0, 3)
  
  # case 4 -> 거꾸로 돌아오면서 hello 발사 (stack 개념)
  def printHello(i, n):
      if i == n:
          print('-------------')
      	return
      
      	printHello(i + 1, n)
          print('Hello!!!')
          
  printHello(0, 3)
  
  # case hard
  cnt = 0
  def printHello(i, n):
      global cnt = 0
      if i == n:
          cnt += 1
          return
          print('-------------')
      	printHello(i + 1, n)           결과 = 1
         # printHello(i + 1, n)		   결과 = 8
          
  printHello(0, 3)
  ```
  
  