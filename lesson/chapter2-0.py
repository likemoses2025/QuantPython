# f string Formatting
name = "JangBuHo"
birth = "1977"

print("f string formatting", f"나의 이름은 {name}이며, {birth}년에 태어났습니다")

# 길이구함
a = "Life is too short"
print(len(a))  # 17

# 문자열 치환
var2 = "퀀트 포트 폴리오 만들기"
var3 = var2.replace(" ", "_")
print(var3)  # 퀀트_포트_폴리오_만들기

# 문자열 나누기
var10 = "퀸트 투자 포트폴리오 만들기"
var11 = var10.split(" ")
print(var11)  # ['퀸트', '투자', '포트폴리오', '만들기']

# 문자열 인덱싱, 슬라이싱
str1 = "Quant"
print("인덱싱 2", str1[2])  # a
print("인덱싱 -2", str1[-2])  # n
print("인덱싱 0:3", str1[0:3])  # Qua   0~2가지의 숫자
print("인덱싱 :2", str1[:2])  # Qa
print("인덱싱 3:", str1[3:])  # nt

# 리스트
a = []
print(type(a))  # type list

list_num = [1, 2, 3]  # list num
list_char = ["1", "2", "3"]  # list char
list_complex = ["a", 2, 3, "b"]  # list complex
list_nest = ["a", 2, 3, ["a", "B"], 8]

# 리스트 인덱싱과 슬라이싱
list_sample = [1, 2, ["a", "b", "c"], "d"]
list_sample[0]  # 1
list_sample[2]  # ["a", "b", "c]
list_sample[2][0]  # "a"
print("list_sample[0:1]", list_sample[0:1])  # 1

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]

a + b  # [1,2,3,4,5,6]
a * 3  # [1,2,3,1,2,3,1,2,3]

# 리스트에 요소 추가
var = [1, 2, 3]
var.append(4)  # [1,2,3,4]

var.append(
    [
        4,
        5,
    ]  # type: ignore
)  # [1,2,3,[4,5]]

var.extend([4, 5])  # [1,2,3,4,5]

# 리스트의 수정과 삭제
var5 = [1, 2, 3, 4, 5]
var5[2] = 10  # 1,2,10,4,5

var5[3] = ["a", "b", "c"]  # type: ignore # [1,2,3,["a", "b", "c"],5]

var5[0:2] = ["가", "나"]  # type: ignore # ["가","나",3,4,5] 0:2는 0~1까지의 데이터를 의미

del var[0]  # [2,3,4,5]

var5[0:1] = []  # [2,3,4,5]

# var5.remove(1)  # [2,3,4,5] remove(x)는 첫번째로 나오는 x을 삭제

var5.pop()  # 5 pop()메소드는 마지막 값을 반환하고 삭제한다. print(var) => [1,2,3,4]


# 리스트의 정렬

var = [2, 4, 1, 3]

var.sort()  # [1,2,3,4]


# 튜플 - 수정과 삭제 불가

var = ()
type(var)  # tuple

var = (1,)  # (1,)

var = (1, 2, ("a", "b"))  # (1,2,("a", "b"))

var[0]  # 1


# 딕셔너리 - 대응관계를 나타내는 자료형, 튜플처럼 순서가 존재하지 않고 키와 값으로 존재

var = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
    "key4": 4,
}

var = {
    "key1": 1,
    "key2": [
        1,
        2,
        3,
    ],
    "key3": ["A", "B", "C", "D", "E", "F"],
}

# 키값을 이용해 값 구하기

var = {"key1": 1, "key2": 2}

var["key1"]  # 1


# 딕셔너리 추가 삭제

var = {"key1": 1, "key2": 2}

var["key3"] = 3  # {"key1": 1, "key2": 2,"key3": 3}

del var["key1"]  # {"key2": 2, "key3": 3}

# 키와 값 구하기

var = {"key1": 1, "key2": 2, "key3": 3}

var.keys()  # dict_keys(["key1", "key2", "key3"])

list(var.keys())  # ["key1", "key2", "key3"]

var.values()  # dict_values([1,2,3])

list(var.values())  # [1,2,3]


# 집합
set1 = set([1, 2, 3])  # 중복 허용 안함,순서 없음
print(set1)  # {1,2,3}

set2 = set("banana")  # {"a","b","n"} 중복된 값을 제거, 순서도 없음

# 합집합,교집합,차집합 - 중복 허용 안함
s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

s1.union(s2)  # {1,2,3,4,5,6} 합집합
s1.intersection(s2)  # {3,4} 교집합
s1.difference(s2)  # {1,2} 차집합


# 불리언

var = True
type(var)  # bool

1 == 1  # True  == 양쪽값이 같은지 비교하는 연산자

1 != 2  # True


# 자료형의 True False

bool(0)  # False
bool(1)  # True
bool(None)  # False
bool("")  # False
bool([])  # False
bool({})  # False
bool(())  # False

bool("Python")  # True
bool([1, 2, 3, 4])  # True
bool({"key1": 1})  # True
bool((1, 2))  # True
