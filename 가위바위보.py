import random
count=0;
win=0;
play=True
#5판3승제
while play:
    player=int(input("가위바위보?:(묵:1 가위:2 보:3)"));
    while(player!=1 and player!=2 and player!=3):
        player=int(input("다시 가위바위보 해줄래?(묵:1 가위:2 보:3)"));
#바위 3 가위 2 보 1
    computer=random.randrange(1,3);
    d=dict()
    d[1]='묵'
    d[2]='가위'
    d[3]='보'
    print("컴퓨터가 낸것은 ",d[computer]='');
    print("너는 ",d[player]);
    
    if(computer==player):
        print("비겼습니다.");
        count+=1;
        
    elif(computer>player):
        print("졌네요");
        count+=1;
        
        if(computer==1):
            print("이겻네요!!!");
            win+=1;
            count+=1;
            
    elif(computer<player):
        if(player==1):
            print(computer , player);
            print("졌네요....");
            count+=1;
            
        print("이겼네요");
        win+=1
        count+=1;
        
    

    if count==5:
        print("게임이 끝났습니다.")
    
        a=int(input("다시하겠습니까??1/2"))
        if(a==1):
            play==True
            count=0
            win=0
        if(a==2):
            play==False
            break
        
            
    if win==3:
        print("당신이 3승으로 이겼습니다.")
        
        a=int(input("다시하겠습니까??1/2"))
        if(a==1):
            play==True
            count=0
            win=0
        if(a==2):
            print('완전히 끝')
            play==False
            
            break
