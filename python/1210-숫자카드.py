# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input()
    card_dic = {}

    # 공백없이 string 형태로 받아온 카드 목록을 반복문을 통해 카운트
    for i in card:
        if i in card_dic:
            card_dic[i] += 1
        else:
            card_dic[i] = 1

    max_cnt = 0
    max_card = 0
    # 딕셔너리 회문으로 최대 빈도인 카드 숫자 구하기
    # items 까먹어서 반복문 두번 돌릴뻔
    for k, v in card_dic.items():
        if v > max_cnt:
            max_card = k
            max_cnt = v
        if v == max_cnt:
            if max_card < k:
                max_card = k

    print(f'#{tc} {max_card} {max_cnt}')
