T = int(input())  # 첫 줄에 주어지는 테스트 케이스 개수 입력

for _ in range(T):
    data = input().split()
    a = float(data[0])
    
    # 두 번째 값부터 끝까지 기호를 하나씩 꺼내서 순서대로 계산
    for op in data[1:]:
        if op == '@':
            a *= 3
        elif op == '%':
            a += 5
        elif op == '#':
            a -= 7
            
    print(f"{a:.2f}")  # 소수점 둘째 자리까지 출력
