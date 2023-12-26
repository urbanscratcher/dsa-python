# 파이썬 배열 기본 문법

# 배열 - 초기화 하는 시점에 정해진 하나의 타입만을 담을 수 있음
# 리스트 - 여러 타입을 하나의 자료구조에 담을 수 있음

# 배열 모듈 불러오기 ----------------
import array as arr

# 배열 초기화 ---------------------
# 정수 배열
int_array = arr.array('i', [1, 2, 3])
print('elements in array : ', end="")
for i in range(0, len(int_array)):
    print(int_array[i], end=" ")
print()

"""
코드    C 언어 타입      파이썬 타입  최소 크기(byte)
'b'  signed char        int        1
'B'  unsigned char      int        1
'u'  Py_UNICODE         unicode    2
'h'  signed short       int        2
'H'  unsigned short     int        2
'i'  signed int         int        2
'I'  unsigned int       int        2
'l'  signed long        int        4
'L'  unsigned long      int        4
'q'  signed long long   int        8
'Q'  unsigned long long int        8
'f'  float              float      4
'd'  double             float      8
"""
# 참고: 리스트, 튜플 등 순회시 인덱스로 0 ~ n-1까지 접근 가능
# 이것을 range(start, end, step) 내장 함수로 접근 인덱스를 생성할 수 있음.
# print()의 경우, 1번의 호출과 함께 new line을 추가함. 이 기본 값은 end 인자를 주면 재설정됨.

# 배열 요소 추가 & 삭제 -------------
# 요소 추가 (n번째 위치에 요소 추가)
int_array.insert(1, 4)
print('elements after insertion : ', end="")
for i in int_array:
    print(i, end=" ")
print()

# 요소 찾아 삭제
int_array.remove(1)
print('elements after delete \'1\' in array : ', end="")
for i in int_array:
    print(i, end=" ")
print()

# 배열 요소 업데이트 ---------------------
int_list = [1, 2, 3, 4, 3, 6, 7, 4, 5, 10]

# list 요소 -> 배열 변환
int_arr = arr.array('i', int_list)
print("elements in array : ")
for i in (int_arr):
    print(i, end=" ")
print()

# 요소 값을 검색해 배열 인덱스 추출 (가장 첫번째로 검색되는 요소)
print("The idx of 1st occurrence of 3 is : ", end="")
print(int_arr.index(3))

# n번째 요소 값 변경
int_arr[4] = 5
print("elements after updation : ", end="")
for i in (int_arr):
    print(i, end=" ")
print()
