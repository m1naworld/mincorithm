'''
재귀함수: 자기 자신을 호출하는 함수

무한루프에 빠지지 않도록 주의!!

재귀 함수와 관련되어 나오는 대표적인 문제
-  팩토리얼! (DP 등 푸는 방법은 다양)
- 회문검사
'''

'''
1. 팩토리얼은 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것을 의미합니다.

예를 들면 아래와 같습니다!
3! 은 3 * 2 * 1 = 6,
4! 는 4 * 3 * 2 * 1 = 4 * 3! = 24

즉,
Factorial(n) = n * Factorial(n - 1)
Factorial(n - 1) = (n - 1) * Factorial(n - 2)
....
Factorial(1) = 1
의 구조입니다!
'''


def factorial(n):
    if n == 1: return 1
    else : return n * factorial(n-1)

print(factorial(5))


