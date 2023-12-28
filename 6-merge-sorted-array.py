"""
<정렬된 배열의 병합>
주어진 정렬된 두 배열(nums1, nums2)을 정렬을 유지하면서 병합

* 추가 설명
- nums1과 nums2의 각 크기는 m과 n개의 요소로 초기화 돼 있음
- nums1은 nums1과 nums2를 병합하기에 충분한 크기로 할당돼 있음 (m+n개)

- leetcode: https://leetcode.com/problems/merge-sorted-array

제한사항
1. 주어진 nums1, nums2의 요소들은 정렬되어 있음
2. nums1의 요소들은 m개
3. nums2의 요소들은 n개
4. nums1 배열의 크기는 n+m

아이디어1 - 정렬 (STL)
1. nums2의 요소를 nums1에서 확보된 추가 공간에 삽입
2. sorted()나 sort() 내장 함수 이용해 정렬
시간 복잡도: O(nlogn)
공간 복잡도: O(n)

* 파이썬 내부 함수 중 sorted()는 Iterable한 객체를 인자로 받는데, 리스트, 스트링, 튜플과 같은 자료구조를 인자로 받으면 정렬이 가능함. 내부적으로 팀정렬(Timsort) 사용.
팀정렬은 기존 삽입 정렬과 병합 정렬을 적절히 조합해 만든 정렬 알고리즘.

아이디어2 - 비교 후 삽입 (two pointers)
1. nums1을 위한 인덱스 포인터 i, nums1의 마지막 요소를 가리킴(m-1)
2. nums2를 위한 인덱스 포인터 j, nums2의 마지막 요소를 가리킴(n-1)
3. 삽입을 위한 포인터 k, nums1 공간 마지막을 가리킴 (m+n-1)
4. 현재 i, j 값 비교
5. 비교해 큰 쪽의 값을 k의 위치에 추가
  - k는 1 감소
  - 비교해 큰 쪽의 인덱스 값이 k에 추가되었으므로 큰 쪽의 인덱스도 1 감소
6. i, j 중 하나라도 0보다 작아지면 비교 중지
7. j가 아직 0보다 크다면 nums1을 가리키고 있는 k 값 감소시키면서 nums1에 삽입
시간 복잡도: O(n+m)
공간 복잡도: O(1)

"""


# 파이썬의 call by value & call by reference
# 인자 중 정수형, 부동 소수형, 문자열, 불리언은 call by value
# 인자 중 리스트, 튜플, 사전 등은 call by reference

def append_element(in_list):
    in_list.append(3)


list_test = [2]
append_element(list_test)
print(f'{list_test}')  # [2, 3]


# 주의할 점은 값을 할당할 때 call by value로 바뀐다는 점
# -> 슬라이스 대입 사용
def append_element(in_list):
    # in_list = [3, 4]  # call by value
    in_list[:] = [3, 4]  # call by reference


list_test = [2]
append_element(list_test)
print(f'{list_test}')  # [3, 4]


# 아이디어1 ---------------
def merge1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # enumerate() 내장함수: 리스트를 인자로 받아 인덱스와 값을 반환해 줌
    for i, v in enumerate(nums2):
        nums1[m + i] = v
    nums1[:] = sorted(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [4, 5, 6]
n = 3
merge1(nums1, m, nums2, n)
print(f'{nums1}')


def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for j in range(n):
        nums1[m+j] = nums2[j]
    nums1.sort()


merge2(nums1, m, nums2, n)
print(f'{nums1}')


# 아이디어2 -----------------
def merge3(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j] and i >= 0:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


# 테스트
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge3(nums1, m, nums2, n)
print(f'{nums1}')
