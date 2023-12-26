# 파이썬 리스트 기본 문법

# 배열 - 초기화 하는 시점에 정해진 하나의 타입만을 담을 수 있음
# 리스트 - 여러 타입을 하나의 자료구조에 담을 수 있음
# is not 메모리 주소 비교, != 값(내용) 비교

# 리스트 초기화 ---------------------
# 빈 리스트
list_empty = []
print(list_empty)

# 요소를 가지는 리스트
list = [1, 2, 3, 4, 5]
print(list)

# 0을 10개 가지는 리스트
list_zeros_1 = [0 for i in range(10)]
print(list_zeros_1)

list_zeros_2 = [0]*10
print(list_zeros_2)

# 리스트 요소 추가 & 삭제 -------------
# 요소 추가
list.append(6)
print(list)

# 배열 요소 추가
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.append(list_2)
print(list_1)

# 배열 요소 확장
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)
print(list_1)

# 요소 삽입 (n번째 위치에 요소 추가)
list = [1, 2, 3]
list.insert(3, 4)
print(list)

# 요소 삭제 (중복시 첫번째로 찾은 값이 삭제됨)
list.remove(2)
print(list)

# 모든 요소 삭제
list.clear()
print(list)

# n번째 요소 삭제
list = [1, 2, 3]
del list[1]
print(list)

# 리스트 요소 접근 ---------------------
# 파이썬에서는 마지막 요소부터 첫번째 요소까지 -1 ~ -n 인덱스로 역순 접근이 가능함
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[9])
print(list[-1])

# 슬라이싱 ([n:m]은 n번째 <= 요소 < m번째)
print(list[3:8])
print(list[5:])
print(list[:-6])

# 콜론 연산을 2개 사용할 시 마지막은 스텝(step)으로 사용
print(list[::2])

# 리스트 역순으로 얻기
print(list[::-1])
print(list[::-2])
