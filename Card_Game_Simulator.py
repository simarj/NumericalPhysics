import random
R=['r' for i in range(0,26)]
B=['b' for i in range(0,26)]
D=R+B
print(D)
for i in range(0,100):
    random.shuffle(D)
print(D)
S=['rrr','rrb','rbr','rbb','bbb','bbr','brb','brr']
Record_player={}
Record_dealer={}
Record={}
for i in S:
    Record_player[i]=0
    Record_dealer[i]=0
for i in S:
    s=S
    s.remove(i)
    for j in s:
        Record[(i,j)]=0
        Record[(j,i)]=0
print(Record)
print(len(Record))
    
   
def judge(dg,pg,D):
    d=D
    s=[d[0],d[1],0]
    for i in range(2,52):
        s[2]=d[i]
        c=s[0]+s[1]+s[2]
        if c == dg:
            p=0
            break
        elif c== pg:
            p=1
            break
        (s[0],s[1])=(s[1],s[2])
    return p
                
            
def bidder(D,n,Record_Player,Record_Dealer):
    Tie=0
    k=0
    while k<n :
        
        random.shuffle(D)
                
        for i in S:
            pg=i
            s=S
            s.remove(i)
            for j in s:
                dg=j
                result=judge(dg,pg,D)
                if result==0:#dealer wins
                    Record_dealer[j]+=1
                    Record[(i,j)]+=1
                elif result==1: # player wins
                    Record_player[j]+=1
                    Record[(j,i)]+=1
                else:
                    Tie+=1
        k+=1
    print('No of games played = \t',n)
    print(Record_player)
    print(Record_dealer)
    
bidder(D,100,Record_player,Record_dealer)
      
     
            
             
                
            
            
            
            
