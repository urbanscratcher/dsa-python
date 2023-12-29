"""
<파스칼의 삼각형>
수학의 이항 계수를 삼각형 형태로 숫자를 배열한 구성
처음 2줄을 제외하고 새로 만들어지는 줄의 새로운 숫자는 윗 줄의 왼쪽 수와 오른쪽 수를 더해 만들어짐. 제일 맷 첫 줄 하나의 숫자는 1.
입력값으로 몇 줄을 만들 것인지를 받아 파스칼의 삼각형을 이차원 배열의 형태로 구성하면 됨.

- leetcode: https://leetcode.com/problems/pascals-triangle

제한사항
1. 입력값은 양의 정수
2. 반환값은 2차원 배열 혹은 리스트

아이디어 - Brute-force
1. 기반 리스트 생성
2. 1번째 리스트 요소를 1로 초기화
3. 입력으로 주어진 행수(numRows)만큼 순회
  - 행의 맨 앞과 맨 뒤 값은 항상 1
  - 순회하면서 해당 줄(line)을 생성하기 위해서는 이전 행의 값을 참조해 더하거나 그대로 사용
시간 복잡도: O(n^2)
공간 복잡도: O(1)

"""


def generate(numRows: int) -> list[list[int]]:
    pascal = []

    if numRows <= 0:
        return pascal

    pascal.append([1])

    for i in range(1, numRows):
        curr = []
        for j in range(i+1):
            num = 1
            if j != 0 and j != i:
                num = pascal[i-1][j-1] + pascal[i-1][j]
            curr.append(num)
        pascal.append(curr)
    return pascal


print(generate(5))


def pyramid(num: int):
    # 피라미드 2차원 배열 생성 & 접근
    pyramidArr = []
    for i in range(num):
        subArr = []
        while i >= 0:
            subArr.append(0)
            i -= 1
        pyramidArr.append(subArr)
    return pyramidArr


print(pyramid(5))
