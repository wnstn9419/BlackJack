import random
import time
# 딜러를 포함한 이원 4명, 코인기능(배팅, 승리시 획득, 패배시 날림), 카드를 받을시 or 버릴시, 차별성, 함수 또는 객체 사용
# sample(list, N) -> list안에 N개를 출력
# 16부터 무조건 배팅 시도 / 15이하는 랜덤으로

def distribute(card_lst): # 카드분배
    global card_list, ai1_card, ai2_card, ai3_card, person_card
    card = random.sample(card_list, 1)
    for number in card:
        card_list.remove(number)
    card_lst.append(card)

def found(n): #카드점수내기
    global ai1_point, ai2_point, ai3_point, person_point
    if n==1:
        for i in range(2):
            for j in range(14):
                if ai1_card[i][0].find(lst_point[j]) != -1:
                    ai1_point += lst_point_plus[j]
                    break
    elif n==2:
        for i in range(2):
            for j in range(14):
                if ai2_card[i][0].find(lst_point[j]) != -1:
                    ai2_point += lst_point_plus[j]
                    break
    elif n==3:
        for i in range(2):
            for j in range(14):
                if ai3_card[i][0].find(lst_point[j]) != -1:
                    ai3_point += lst_point_plus[j]
                    break
    else:
        for i in range(2):
            for j in range(14):
                if person_card[i][0].find(lst_point[j]) != -1:
                    person_point += lst_point_plus[j]
                    break

def judgment(n):
    if n >= 16 and n < 22:
        return 1
    if n > 21:
        return 0
    m = random.sample(bol, 1)
    return m[0]


card_list = ['♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K','♠A',
'♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K','♣A', '♥2', '♥3', 
'♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', '♥A', '◆2', '◆3', 
'◆4', '◆5', '◆6', '◆7', '◆8', '◆9', '◆10', '◆J', '◆Q', '◆K', '◆A']
lst_point = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'Q', 'J', 'K']
lst_point_plus = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ai1_card, ai2_card, ai3_card, person_card = [], [], [], [] # 카드 저장
ai1_point, ai2_point, ai3_point, person_point = 0, 0, 0, 0 # 현재 점수
ai1_coin, ai2_coin, ai3_coin, person_coin, total_coin = 10, 10, 10, 10, 0 # 코인 저장
ai1_attend, ai2_attend, ai3_attend, person_attend = 0, 0, 0, 0
bol = [0, 1]
# ai1에 카드 부여후 card_list에서 해당 카드 제거
print('첫 번째 카드 전달중....')
#time.sleep(3)
print('전달 완료')

# 첫 번째 카드 전달
distribute(ai1_card)
distribute(ai2_card)
distribute(ai3_card)
distribute(person_card)

#time.sleep(10)

print('두 번째 카드 전달중....')
#time.sleep(3)
print('전달 완료')

# 두 번째 카드 전달
distribute(ai1_card)
distribute(ai2_card)
distribute(ai3_card)
distribute(person_card)

print(ai1_card)
print(ai2_card)
print(ai3_card)
print(person_card)

# 점수내기
for i in range(1, 5):
    found(i)

print(ai1_point)
print(ai2_point)
print(ai3_point)
print(person_point)

# 참가여부
ai1_attend = judgment(ai1_point)
print(ai1_attend)
ai2_attend = judgment(ai2_point)
print(ai2_attend)
ai3_attend = judgment(ai3_point)
print(ai3_attend)
person_attend = judgment(person_point)
print(person_attend)