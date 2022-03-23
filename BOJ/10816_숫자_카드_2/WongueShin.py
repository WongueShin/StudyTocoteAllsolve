from sys import stdin

def input():
    return stdin.readline().rstrip()

N = int(stdin.readline())
cards = list(map(int, input().split()))
M = int(stdin.readline())
call_list = list(map(int, input().split()))
card_dict = {}

for card in cards:
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] += 1

return_str = ''
for call in call_list:
    if call not in card_dict:
        return_str += ' 0'
    else:
        return_str += (' '+str(card_dict[call]))

return_str = return_str.strip()
print(return_str)
