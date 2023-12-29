"""
<배열에서 다수의 요소 찾기>
정수형 배열이 주어졌을 때 다수의 요소 찾기. 다수의 요소는 배열 내에서 floor(n/2)번을 초과하여 나타나는 요소를 말함. 예를 들어 배열 요소 총개수가 9개라면 n/2는 4.5이다. 결국 5번 이상 나타나는 요소를 찾으면 된다. 배열은 항상 1개 이상의 요소를 가지고 있으며 다수의 수가 무조건 하나 존재한다고 가정하자.

입력값이 [2,1,2]라면 다수의 요소는 2.

- leetcode: https://leetcode.com/problems/majority-element/

제한사항
1. 입력값은 정수형 배열
3. 배열은 1개 이상의 요소를 가짐
4. 다수의 수는 무조건 1개가 존재

아이디어1 - Brute-force
1. 배열 순회
2. 각 요소와 다른 모든 요소들을 비교해 배열에 몇 개가 들어 있는지 파악
3. 개수를 세면서 다수의 수 조건에 맞는 숫자가 있으면 반환
시간 복잡도: O(n^2) 
공간 복잡도: O(1)

아이디어2 - Hash Table
1. 해시 테이블에서 키 항목으로는 배열의 요소로 하고, 값 항목으로는 횟수 지정
2. 배열 순회
3. 배열 순회하면서 해당 요소를 해시 테이블에서 찾는다
  - 값이 있다면 해당 요소를 키값으로 하는 값 항목을 꺼내 1을 더해 업데이트
  - 값이 없다면 해당 요소를 키 항목으로 두고 1의 값으로 추가
4. 값을 업데이트한 후 다수의 수 조건에 맞는 숫자 반환
시간 복잡도: O(n)
공간 복잡도: O(n)
  - 최악의 경우 요소만큼 해시 테이블이 만들어져야 함

아이디어3 - 정렬
1. 배열을 정렬
2. 가운데 수를 반환
시간 복잡도: O(nlogn)
공간 복잡도: O(1)

"""


def majorityElement1(nums: list[int]) -> int:
    majorityCount = int(len(nums)/2)
    for i, v in enumerate(nums):
        count = 0
        for j, w in enumerate(nums[i:], start=i):
            if (w == v):
                count += 1
        if (count > majorityCount):
            return v
    return -1


print(majorityElement1([6, 5, 5]))  # 5


def majorityElement2(nums: list[int]) -> int:
    majorityCount = int(len(nums)/2)
    hashmap = {}

    for n in nums:
        if hashmap.get(n) != None:
            hashmap[n] = hashmap[n]+1
        else:
            hashmap[n] = 1

        if hashmap[n] > majorityCount:
            return n

    return -1


print(majorityElement2([2, 1, 1]))  # 1


def majorityElement3(nums: list[int]) -> int:
    return sorted(nums)[int(len(nums)/2)]


print(majorityElement3([2, 1, 1]))  # 1
