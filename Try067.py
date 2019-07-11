from random import randrange

coin_user, coin_bot = 10, 10
rounds_of_game = 0


def bet(dice, wager):
    if dice == 7:
        print(f'This dice is {dice};\nDraw!\n')
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'This dice is {dice};\n You WIN!\n')
            return 1
        else:
            print(f'This dice is {dice};\nYou LOST!\n')
            return -1
    elif dice > 7:
        if wager == 's':
            print(f'This dice is {dice};\nYou LOST!\n')
            return -1
        else:
            print(f'This dice is {dice};\nYou WIN!\n')
            return 1


while True:
    print(f'You:{coin_user}\t Bot:{coin_bot}')
    dice = randrange(2, 13)
    wager = input("What's your bet?\n")
    # wager = 'sb'[randrange(2)]
    if wager == 'q':
        break
    elif wager in 'bs':
        result = bet(dice, wager)
        coin_user += result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print("Woops,you've LOST ALL,and game over!")
        break
    elif coin_bot == 0:
        print("Woops,the robot've LOST ALL, and game over!")
        break

print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user} coins now.\nBye!")

# 为什么用 wager = 'sb'[randrange(2)]测试，每次都是coin_bot赢呢？
# 忘记写最后一个break了
