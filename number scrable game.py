a=[1,2,3,4,5,6,7,8,9]
player=1
print("welcome in number scrable game")
print(a[0],a[1],a[2])
print(a[3],a[4],a[5])
print(a[6],a[7],a[8])
p1=[]
p2=[]
while True:
    if player==1:
        print("player",player,"choose a number")
        x = int(input())
        while True:
            if x in a:
                break
            else:
                print("this number isn't in the list")
                x = int(input("enter another number\n "))
        p1.append(x)
        a.remove(x)
        print(a)
        if len(p1) == 3:
            if p1[0] + p1[1] + p1[2] == 15:
                print("congratulation\nplayer", player, "win")
                break
            if len(p1) == 4:
                if p1[0] + p1[1] + p1[3] == 15 or p1[0] + p1[2] + p1[3] == 15 or p1[1] + p1[2] + p1[3] == 15:
                    print("congratulation\nplayer 1 win")
                    break
            if len(p1) == 5:
                if p1[0] + p1[1] + p1[4] == 15 or p1[0] + p1[2] + p1[4] == 15 or p1[0] + p1[3] + p1[4] == 15 or p1[1] + p1[2] + p1[4] == 15 or p1[1] + p1[3] + p1[4] == 15 or p1[2] + p1[3] + p1[4] == 15:
                    print("congratulation\nplayer 1 win")
                    break
    if player==2:
        print("Player",player,"Choose a number")
        y=int(input())
        while True:
            if y in a:
                break
            else:
                print("this number isn't in the list")
                y=int(input("enter another number\n "))
        p2.append(y)
        a.remove(y)
        print(a)
        if len(p2) == 3:
            if p2[0] + p2[1] + p2[2] == 15:
                print("congratulation\nplayer 2 win")
                break
        if len(p2) == 4:
            if p2[0] + p2[1] + p2[3] == 15 or p2[0] + p2[2] + p2[3] == 15 or p2[1] + p2[2] + p2[3] == 15:
                print("congratulation\nplayer 2 win")
                break
    if player==1:
        player=2
    elif player==2:
        player=1
    if len(p1)==5 and len(p2)==4:
        print(" the game is a draw")
        break
