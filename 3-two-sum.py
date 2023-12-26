"""
<두 수의 합 찾기>
주어진 정수형 배열에서 2개의 숫자를 선택해 더한 값이 특정 목푯값을 만들 때, 선택한 정수 2개의 인덱스 값으로 이루어진 배열을 반환하라.

입력값: nums = [2, 7, 10, 19], target = 9
출력값: [0, 1]

- leetcode: https://leetcode.com/problems/two-sum
- hackerrank: https://www.hackerrank.com/challenges/pairs/problem
- 백준: https://www.acmicpc.net/problem/3273


제한사항
1. 정수형 배열
2. 두 수의 합이 정수형을 초과할 수 있는가?
  - 언급 X
3. 두 수의 합이 배열 내에 무조건 존재?
  - 무조건 존재
4. 요소 중복 불가


아이디어1 - 모든 경우의 수(Brute-force)
1. 배열의 모든 요소의 조합을 찾는다
  - 루프는 i = 0 ~ n, j = i+1 ~ n으로 이중 루프
  - 1번째 루프(n번), 2번째 루프(n-1번)을 기준으로 n*(n-1)번 계산
2. 해당 조합으로 목푯값과 비교해 같다면
  - 해당 루프를 종료, 각 값을 가진 인덱스 반환
시간 복잡도: O(n^2)
공간 복잡도: O(1)


아이디어2 - 해시 테이블
1. 해시 테이블 구성
  - 키 값으로는 배열 요소, 값으로는 요소의 인덱스로 구성
2. 각 요소를 순회하면서
  - 목푯값 - 현재 요소 = 다른 요소
  - 해시 테이블에서 다른 요소 값 찾기
  - 다른 요소가 해시 테이블에 있다면, 현재 요소의 인덱스와 해시 테이블의 값(인덱스) 반환
  - 다른 요소가 없다면, 현재 요소를 해시 테이블의 키 값으로 넣고 인덱스를 해시 테이블의 값 항목으로 추가
시간 복잡도: O(n)
공간 복잡도: O(n)
  - 해시 테이블을 생성해 최대로 모든 요소(n)을 담아야 함
"""


def twoSum1(nums: list[int], target: int) -> list[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]
    return [-1, -1]


def twoSum2(nums: list[int], target: int) -> list[int]:
    hashtable_dict = {}
    for i in range(0, len(nums)):
        value = target - nums[i]
        if (hashtable_dict.get(value) is not None) and (hashtable_dict[value] != i):
            return sorted([i, hashtable_dict[value]])
        hashtable_dict[nums[i]] = i
    return [-1, -1]


# 테스트
nums = [2, 7, 10, 19]
target = 9
print(twoSum1(nums, target))
print(twoSum2(nums, target))
