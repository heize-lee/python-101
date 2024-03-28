# 기본 자료형 실습:
# 1. 정수형 
my_integer = 12
print(my_integer)
print(type(my_integer)) #class 'int'

# 2. 부동소수점
my_float = 12.1
print(my_float)
print(type(my_float)) #class 'float'

# 3. 문자열
my_string = "Hello, Python!"
print(my_string)
print(type(my_string)) #class 'str'

# 4. [List]
my_list = [1,2,3,'python',4,5]
print(my_list)
print(type(my_list)) #class 'list'

# 4.1 List index - 1, python
print(my_list[0])
print(my_list[3])

# 5. (Tuple) : 한번 생성하면 변경할 수 없다.
my_tuple = (1,2,3,'python',4.5)
print(my_tuple)
print(type(my_tuple)) #class 'tuple'

# 6. {Dict:ionary}
my_dict = {'name':'python', 'type':'programming language'}
print(my_dict)
print(type(my_dict)) #class 'dict'

# 7. {Set} : 중복을 허용하지 않음
my_set = {1,1,3,3,5}
print(my_set)
print(type(my_set)) #class 'set'

# 문자 자료형 실습:
# 1. len() : 문자열의 길이를 반환합니다.
print(len(my_string))

# 2. str.upper() : 모든 문자를 대문자로 변환합니다.
print(my_string.upper())

# 3. str.lower() : 모든 문자를 소문자로 변환합니다.
print(my_string.lower())

# 4. str.capitalize() : 문자열의 첫 글자'만' 대문자로 변환합니다.
print(my_string.capitalize())

# 5. str.title() : 문자열의 '각 단어'의 첫 글자를 대문자로 변환합니다.
print(my_string.title())

# 6. str.strip() : 문자열 양쪽의 공백을 제거합니다. l(eft)strip(), r(ight)strip()
my_space = " s p a c e "
print(my_space.strip())

# 7. str.find() : 부분 문자열이 처음으로 나타나는 위치를 반환합니다. 찾지못하면 -1을 반환합니다.
print(my_string.find('Hello'))
print(my_string.find('World'))

# 8. str.replace() : 문자열 내의 특정 문자 또는 문자열을 다른 문자 또는 문자열로 교체합니다. 원본은 변하지 않습니다.
my_string = "Hello, Python!"
print(my_string.replace('Python!', 'World'))
print(my_string)

# 9. str.split() : 문자열을 특정 구분자로 분리하여 리스트로 반환합니다.
my_apple = "Mac, Airpods, iPhone, Apple Watch, ..."
print(my_apple.split(','))
print(type(my_apple))

# 10. str.join() : 문자열 리스트를 하나의 문자열로 결합합니다. 각 문자열 사이에 지정한 문자열을 삽입합니다.
print(','.join(my_string))

# Unpacking
my_tuple = (1,2,3)
x,y,z = my_tuple
print('x 좌표', x)
print('y 좌표', y)
print('z 좌표', z)

# List Unpacking 
my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)

# Set Unpacking : 집합은 순서가 없기 때문에 언패킹의 결과는 예측할 수 없습니다.
my_set = {1, 2, 3}
a, b, c = my_set
print(a, b, c)

# Unpacking and asterisk (*) usage
my_list = [1, 2, 3, 4, 5]
a, *b, c = my_list
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Slicing : 리스트변수[시작인덱스:끝인덱스]
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:6])  # [2, 3, 4, 5]
print(my_list[:5])  # [0, 1, 2, 3, 4]
print(my_list[5:])  # [5, 6, 7, 8, 9]
print(my_list[:])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Negative
# 끝에서 세 번째 요소부터 마지막 요소까지 선택
print(my_list[-3:])  # [7, 8, 9]
# 끝에서 네 번째 요소부터 끝에서 두 번째 요소까지 선택
print(my_list[-4:-1])  # [6, 7, 8]

# Step
# 전체 리스트에서 하나 건너 하나씩 요소 선택
print(my_list[::2])  # [0, 2, 4, 6, 8]
# 인덱스 1부터 시작하여 하나 건너 하나씩 요소 선택
print(my_list[1::2])  # [1, 3, 5, 7, 9]
# 리스트를 역순으로 선택
print(my_list[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]