##ex01_01_04
def move(n,a,b,c):
    if n == 1:
        print(a,'->',c)
    else:
        move(n-1,a,c,b)
        print(a,'->',c)
        move(n-1,b,a,c)
def main():
    n = eval(input("请输入盘子数："))
    move(n,'A','B','C')
main()
