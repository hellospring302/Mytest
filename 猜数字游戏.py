import random
def game(start,end):
    print('给定的范围为{}-{}'.format(start,end))
    dround = random.randint(start,end)
    while True:
        pp = eval(input("你猜的数字是多少:"))
        if pp < dround:
            print('小了，再猜！')
            start = pp
            print('范围在{}-{}'.format(start,end))
            continue
        elif pp > dround:
            print('大了，再猜！')
            end = pp
            print('范围在{}-{}'.format(start,end))
            continue
        else:
            print('你猜中了！')
            break
def main():
    start,end=eval(input('输入范围，逗号隔开:'))
    game(start,end)

main()
