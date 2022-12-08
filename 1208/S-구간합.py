# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_arr = []
    # arr 길이 만큼 반복
    for i in range(N-M+1):
        # M의 구간의 합 구하기
        sum_reset = 0
        for j in range(M):
            sum_reset += arr[i+j]
        sum_arr.append(sum_reset)

    max_value = sum_arr[0]
    min_value = sum_arr[0]

    # 구간 합의 최댓값, 최솟값 구하기
    # max, min 사용가능
    for i in range (len(sum_arr)):
        if max_value < sum_arr[i]:
            max_value = sum_arr[i]
        if min_value > sum_arr[i]:
            min_value = sum_arr[i]
    # 최대값 - 최소값
    result = max_value - min_value

    print(f'#{tc} {result}')





