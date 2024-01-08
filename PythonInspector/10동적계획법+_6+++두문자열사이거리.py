'''
주어진 문자열 s1이 s2가 되기 위해 문자를 제거 및 추가하기 위한 최소 횟수를 반환하세요.

두 문자열 사이의 거리
두 문자열 s1, s2가 주어진다. 이제 s1에서 문자 하나를 추가하거나 제거할 수 있으며, 이를 반복함으로써 s2를 얻고싶다고 하자. 
예를 들어, s1 = “abc”, s2 = “bdcf” 라고 하면, s1에서 a를 제거하고 d를 추가, 그리고 f를 추가하면 s2를 얻을 수 있다. 
즉, 다음과 같은 경로로 s1에서 s2를 얻을 수 있다. “abc” -> “bc” -> “bdc” -> “bdcf”

두 문자열 s1, s2 사이의 거리란, s1에서 s2를 만들기 위해 필요한 문자 삽입, 삭제 횟수의 최소값으로 정의된다. 
예를 들어, s1 = “abc”, s2 = “bdcf”라면, 두 문자열의 거리는 3이다. 
왜냐하면, s1에서 문자의 추가 및 삭제를 3번 하면 s2를 얻을 수 있기 때문이며, 이보다 더 적은 연산을 통해서는 s2를 얻을 수 없다.
두 문자열이 주어질 때, 두 문자열 사이의 거리를 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에 문자열 s1, 두 번째 줄에 문자열 s2가 주어진다. 문자열의 길이는 2000을 넘지 않는다.

출력
두 문자열 사이의 거리를 출력한다.

입력 예시
abc
bdcf

출력 예시
3
'''
def strDistance(s1, s2) :


    return 0

#main.py
import sys
from strDistance import strDistance


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    s1 = input()
    s2 = input()

    print(strDistance(s1, s2))

if __name__ == "__main__":
    main()
