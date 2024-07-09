# Вам даны три числа 𝑎, 𝑏, и 𝑐. Определите, является ли одно суммой двух других

# t=int(input('Введите количество тестовых случаев'))
#
# for _ in range(t):
#     a, b, c = map(int, input('Введите числа').split())
#     if a==b+c or b==a+c or c==a+b:
#         print('YES')
#     else:
#         print('NO')


t = int(input())

for _ in range(t):
    a, b, c = sorted(map(int, input().split()))

    if a + b == c or a == b + c:
        print('YES')
    else:
        print('NO')