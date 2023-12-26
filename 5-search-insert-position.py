"""
<배열에서 삽입 위치 찾기>
정렬된 배열과 목푯값이 주어짐. 목푯값을 찾으면 배열의 해당 인덱스를 반환하고, 못 찾으면 정렬된 배열이 되도록 목표값이 배열에 들어가야 하는 인덱스를 구하는 문제

입력값: nums=[1,2,3,4,5], target=3
출력값: 2

입력값: nums=[1,4,5,6], target=3
출력값: 1

- leetcode: https://leetcode.com/problems/search-insert-position

제한사항
1. 정수형 배열
2. 정수형 target 변수
3. 배열의 값은 정수(음수, 0, 양수)
4. 배열은 정렬돼 있음
5. 배열의 크기가 매우 클 수 있음

아이디어1 - Brute-force
1. 배열의 각 요소를 인덱스0부터 순회
2. 순회하면서 target 값보다 같거나 큰 경우 순회를 중단
3. 중단된 시점의 인덱스 반환하고
시간 복잡도: O(n)
공간 복잡도: O(1)

아이디어2 - 해시 테이블
1. 배열 요소를 이진 탐색으로 접근
2. 요소를 찾으면 해당 인덱스 반환
3. 찾지 못하고 이진 탐색을 종료하면, 최종 접근했던 낮은 인덱스 값 반환
시간 복잡도: O(log n)
공간 복잡도: O(1)

이 문제는 target 값을 입력으로 주어진 배열에 넣을 위치만 파악하는 것이지, 해당 값을 배열에 넣어 업데이트하는 문제가 아니다. 이 경우 이진 탐색을 고려하면 순차 접근보다 효율적인 방법이 될 수 있다.

"""


def searchInsert1(nums: list[int], target: int) -> int:
    idx = 0
    while idx < len(nums):
        if target <= nums[idx]:
            return idx
        idx += 1

    return idx


def searchInsert2(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            high = mid - 1
        if nums[mid] < target:
            low = mid + 1

    return low


nums = [1, 2, 3, 4, 5]
target = 3
print(searchInsert1(nums, target))
print(searchInsert2(nums, target))

nums = [1, 4, 5, 6]
target = 3
print(searchInsert1(nums, target))
print(searchInsert2(nums, target))
