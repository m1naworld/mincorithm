'''
회문은 똑바로 읽으나 거꾸로 읽으나 똑같은 단어나 문장을 의미합니다.

Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.
'''

# input = "abcba"
input = "소주만병만주소"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

print(is_palindrome(input))