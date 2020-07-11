
def forbidden_move(curPlayer,noncurPlayer,x,y,width):
    # up, right-up, right, right-down, down, left-down, left, left-up
    # res=[0]*8
    adjacent=[0]*8
    adjacent_blank=[0]*8
    jump_one=[0]*8
    jump_blank=[0]*8
    jump_blank_same=[0]*8

    #  up
    # for i in range(x,8):
    #     if curPlayer[i][y]
    i=x-1
    while i>=0 and curPlayer[i][y]==1:  # board[i][y] is black
        i-=1
        adjacent[0]+=1
    while i>=0 and noncurPlayer[i][y]==0: # board[i][y] is blank
        i-=1
        adjacent_blank[0]+=1
    while i>=0 and curPlayer[i][y]==1: # board[i][y] is black
        i-=1
        jump_one[0]+=1
    while i>=0 and noncurPlayer[i][y]==0: # board[i][y] is blank
        i-=1
        jump_blank[0]+=1
    while i>=0 and curPlayer[i][y]==1: # board[i][y] is black
        i-=1
        jump_blank_same[0]+=1
    
    # right-up
    i=x-1
    j=y+1
    while j<width and i>=0 and curPlayer[i][j]==1: # board[i][j] is black
        j+=1
        i-=1
        adjacent[1]+=1
    while j<width and i>=0 and noncurPlayer[i][y]==0: # board[i][j] is blank
        j+=1
        i-=1
        adjacent_blank[1]+=1
    while j<width and i>=0 and curPlayer[i][j]==1: # board[i][j] is black
        j+=1
        i-=1
        jump_one[1]+=1
    while j<width and i>=0 and noncurPlayer[i][y]==0: # board[i][j] is blank
        j+=1
        i-=1
        jump_blank[1]+=1
    while j<width and i>=0 and curPlayer[i][j]==1: # board[i][j] is black
        j+=1
        i-=1
        jump_blank_same[1]+=1
    
    # right
    j=y+1
    # print(noncurPlayer)
    # print(curPlayer)
    while j<width and curPlayer[x][j]==1: # board[x][j] is black
        j+=1
        adjacent[2]+=1
    while j<width and noncurPlayer[x][j]==0: # board[x][j] is blank
        j+=1
        adjacent_blank[2]+=1
    while j<width and curPlayer[x][j]==1: # board[x][j] is black
        j+=1
        jump_one[2]+=1
    while j<width and noncurPlayer[x][j]==0: # board[x][j] is blank
        j+=1
        jump_blank[2]+=1
    while j<width and curPlayer[x][j]==1: # board[x][j] is black
        j+=1
        jump_blank_same[2]+=1
    
    # right down
    j=y+1
    i=x+1
    while j<width and i<width and curPlayer[i][j]==1: # board[i][j] is black
        i+=1
        j+=1
        adjacent[3]+=1
    while j<width and i<width and noncurPlayer[i][j]==0: # board[i][j] is blank
        i+=1
        j+=1
        adjacent_blank[3]+=1
    while j<width and i<width and curPlayer[i][j]==1: # board[i][j] is black
        i+=1
        j+=1
        jump_one[3]+=1
    while j<width and i<width and noncurPlayer[i][j]==0: # board[i][j] is blank
        i+=1
        j+=1
        jump_blank[3]+=1
    while j<width and i<width and curPlayer[i][j]==1: # board[i][j] is black
        i+=1
        j+=1
        jump_blank_same[3]+=1
    
    # down 
    i=x+1
    while i<width and curPlayer[i][y]==1: # board[i][y] is black
        i+=1
        adjacent[4]+=1
    while i<width and noncurPlayer[i][y]==0: # board[i][y] is blank
        i+=1
        adjacent_blank[4]+=1
    while i<width and curPlayer[i][y]==1: # board[i][y] is black
        i+=1
        jump_one[4]+=1
    while i<width and noncurPlayer[i][y]==0: # board[i][y] is blank
        i+=1
        jump_blank[4]+=1
    while i<width and curPlayer[i][y]==1: # board[i][y] is black
        i+=1
        jump_blank_same[4]+=1
    
    # left-down
    i=x+1
    j=y-1
    while i<width and j>=0 and curPlayer[i][j]==1: # board[i][j] is black
        i+=1
        j-=1
        adjacent[5]+=1
    while i<width and j>=0 and noncurPlayer[i][j]==0: # board[i][j] is blank
        i+=1
        j-=1
        adjacent_blank[5]+=1
    while i<width and j>=0 and curPlayer[i][j]==1: # board[i][j] is black
        i+=1
        j-=1
        jump_one[5]+=1
    while i<width and j>=0 and noncurPlayer[i][j]==0: # board[i][j] is blank
        i+=1
        j-=1
        jump_blank[5]+=1
    while i<width and j>=0 and curPlayer[i][j]==1: # board[i][j] is black
        i+=1
        j-=1
        jump_blank_same[5]+=1

    # left 
    j=y-1
    while j>=0 and curPlayer[x][j]==1: # board[x][j] is black
        j-=1
        adjacent[6]+=1
    while j>=0 and noncurPlayer[x][j]==0: # board[x][j] is blank
        j-=1
        adjacent_blank[6]+=1
    while j>=0 and curPlayer[x][j]==1: # board[x][j] is black
        j-=1
        jump_one[6]+=1
    while j>=0 and noncurPlayer[x][j]==0: # board[x][j] is blank
        j-=1
        jump_blank[6]+=1
    while j>=0 and curPlayer[x][j]==1: # board[x][j] is black
        j-=1
        jump_blank_same[6]+=1
    
    # left-up
    j=y-1
    i=x-1
    while i>=0 and j>=0 and curPlayer[i][j]==1: # board[i][j] is black
        i-=1
        j-=1
        adjacent[7]+=1
    while i>=0 and j>=0 and noncurPlayer[i][j]==0: # board[i][j] is blank
        i-=1
        j-=1
        adjacent_blank[7]+=1
    while i>=0 and j>=0 and curPlayer[i][j]==1: # board[i][j] is black
        i-=1
        j-=1
        jump_one[7]+=1
    while i>=0 and j>=0 and noncurPlayer[i][j]==0: # board[i][j] is blank
        i-=1
        j-=1
        jump_blank[7]+=1
    while i>=0 and j>=0 and curPlayer[i][j]==1: # board[i][j] is black
        i-=1
        j-=1
        jump_blank_same[7]+=1

    for i in range(4):
        if adjacent[i]+adjacent[i+4]==4:
            return 0

    cnt3=0
    cnt4=0
    for i in range(4):
        if adjacent[i]+adjacent[i+4]>4:
            return 1
        elif adjacent[i]+adjacent[i+4]==3:
            flag4=False
            if adjacent_blank[i]>0 and check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                    flag4=True
            if adjacent_blank[i+4]>0 and check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                    flag4=True
            if flag4==True:
                cnt4+=1
        elif adjacent[i]+adjacent[i+4]==2:
            flag3=False
            if adjacent_blank[i]==1 and jump_one[i]==1 and check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                cnt4+=1
            if adjacent_blank[i+4]==1 and jump_one[i+4]==1 and check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                cnt4+=1
            if (adjacent_blank[i]>=2 and jump_one[i]==0) and \
                (adjacent_blank[i+4]>=1 and jump_one[i+4]==0) and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                flag3=True
            if (adjacent_blank[i]>=1 and jump_one[i]==0) and \
                (adjacent_blank[i+4]>=2 and jump_one[i+4]==0) and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                flag3=True
            if flag3==True:
                cnt3+=1
        elif adjacent[i]+adjacent[i+4]==1:
            if adjacent_blank[i]==1 and jump_one[i]==2 and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                    cnt4+=1
            if adjacent_blank[i+4]==1 and jump_one[i+4]==2 and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                    cnt4+=1
            if adjacent_blank[i]==1 and jump_one[i]==1 and \
                (jump_blank[i]>=1 and jump_blank_same[i]==0) and \
                (adjacent_blank[i+4]>=1 and jump_one[i+4]==0) and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                cnt3+=1
            if adjacent_blank[i+4]==1 and jump_one[i+4]==1 and \
                (adjacent_blank[i]>=1 and jump_one[i]==0) and \
                (jump_blank[i+4]>=1 and jump_blank_same[i+4]==0) and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                cnt3+=1
        elif adjacent[i]+adjacent[i+4]==0:
            if adjacent_blank[i]==1 and jump_one[i]==3 and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                cnt4+=1
            if adjacent_blank[i+4]==1 and jump_one[i+4]==3 and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                cnt4+=1
            if adjacent_blank[i]==1 and jump_one[i]==2 and \
                (jump_blank[i]>=1 and jump_blank_same[i]==0) and \
                (adjacent_blank[i+4]>=1 and jump_one[i+4]==0) and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i],i,width)==0:
                cnt3+=1
            if adjacent_blank[i+4]==1 and jump_one[i+4]==2 and \
                (adjacent_blank[i]>=1 and jump_one[i]==0) and \
                (jump_blank[i+4]>=1 and jump_blank_same[i+4]==0) and \
                check_forbid(curPlayer,noncurPlayer,x,y,adjacent[i+4],i+4,width)==0:
                cnt3+=1
    if cnt4>=2 or cnt3>=2:
        return 1
    return 0




def check_forbid(curPlayer,noncurPlayer,x,y,adjacent,direction,width):
    i,j=0,0
    adjacent+=1
    if direction>=4:
        adjacent=-adjacent
    if direction%4==0:
        i=x-adjacent
        j=y
    elif direction%4==1:
        i=x-adjacent
        j=y+adjacent
    elif direction%4==2:
        i=x
        j=y+adjacent
    elif direction%4==3:
        i=x+adjacent
        j=y+adjacent
    origin=curPlayer[x][y]
    origin1=curPlayer[i][j]
    curPlayer[x][y]=1
    curPlayer[i][j]=1
    res=forbidden_move(curPlayer,noncurPlayer,i,j,width)
    curPlayer[x][y]=origin
    curPlayer[i][j]=origin1
    return res
