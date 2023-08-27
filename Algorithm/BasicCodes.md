## 목차 [[돌아가기]](./README.md)
1. [sum( iterable )](#1-sum-iterable---리스트-튜플-세트-딕셔너리-등-iterable-자료들의-숫자-데이터들을-더해준다)
2. [len( object )](#2-len-object---문자열-리스트-튜플-세트-딕셔너리-등의-데이터의-크기-를-나타낸다)
3. [min( arg, arg, ... )](#3-min-arg-arg-arg----여러-입력값들-중에-최솟값을-골라낸다-리스트-튜플-등-iterable-을-입력할-수-있다)
4. [max( arg, arg, ... )](#4-max-arg-arg-arg----여러-입력값들-중에-최댓값을-골라낸다-리스트-튜플-등-iterable-을-입력할-수-있다)

## 1. 내장함수를 대체하는 기본 코드
#### 1. sum( iterable ) : 리스트, 튜플, 세트, 딕셔너리 등 iterable 자료들의 '숫자' 데이터들을 더해준다. 
```python
# 대체 코드
my_list = [1, 2, 3, 4, 5]

my_sum = 0          # 더한 숫자를 저장할 공간

for i in my_list:   # iterable 을 모두 순회하며
    my_sum += i     # 모든 값을 더한다. 
```
#### 2. len( object ) : 문자열, 리스트, 튜플, 세트, 딕셔너리 등의 데이터의 '크기' 를 나타낸다.
```python
# 대체 코드
my_str = 'abcd'

my_len = 0          # 길이를 저장할 공간

for i in my_str:    # iterable 을 모두 순회하며
    my_len += 1     # 1씩 더한다.
```
#### 3. min( arg, arg, arg, ... ) : 여러 입력값들 중에 최솟값을 골라낸다. 리스트, 튜플 등 iterable 을 입력할 수 있다.
```python
# 대체 코드
my_list = [1, 2, 3, 4, 5, 6]

my_min = float('int')   # 최소값을 저장할 공간, 초기값을 매우 '큰' 값으로 지정해야 한다.

for i in my_list:       # iterble 을 순회하면서,
    if my_min < i:      # 현재 값보다 새로 들어온 값이 작으면
        my_min = i      # my_min에 저장한다.
```
#### 4. max( arg, arg, arg, ... ) : 여러 입력값들 중에 최댓값을 골라낸다. 리스트, 튜플 등 iterable 을 입력할 수 있다.
```python
# 대체 코드
my_list = [1, 2, 3, 4, 5, 6]

my_max = 0              # 최소값을 저장할 공간, 초기값을 매우 '작은' 값으로 지정해야 한다.

for i in my_list:       # iterble 을 순회하면서,
    if my_max > i:      # 현재 값보다 새로 들어온 값이 크면
        my_max = i      # my_max에 저장한다.
```

## 2. 