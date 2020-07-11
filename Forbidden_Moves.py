import numpy as np

# Player 1 with X
# Player 2 with O

#        0       1       2       3       4       5       6       7

#    7   X       _       _       _       _       _       _       _    


#    6   X       O       _       _       _       O       _       _    


#    5   _       _       O       _       O       _       _       _    


#    4   X       _       _       _       X       _       _       _    


#    3   _       _       O       _       O       _       _       _    


#    2   _       _       _       _       _       O       _       _    


#    1   _       _       _       _       _       _       O       _    


#    0   _       _       _       _       _       _       _       _    


# noncurPlayer=[[1., 0., 0., 0., 0., 0., 0., 0.],\
#               [1., 0., 0., 0., 0., 0., 0., 0.],\
#               [0., 0., 0., 0., 0., 0., 0., 0.],\
#               [1., 0., 0., 0., 0., 0., 0., 0.],\
#               [0., 0., 0., 0., 0., 0., 0., 0.],\
#               [1., 0., 0., 0., 0., 0., 0., 0.],\
#               [0., 0., 0., 0., 0., 0., 0., 0.],\
#               [0., 0., 0., 0., 0., 0., 0., 0.]]

# curPlayer=[[0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 1., 0., 0., 0., 1., 0., 0.],\
#            [0., 0., 1., 0., 1., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 1., 0., 1., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 1., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.]]

# last_move=[[0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 1., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.],\
#            [0., 0., 0., 0., 0., 0., 0., 0.]]

# which player
#  [[0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0. 0. 0. 0.]]]

# 检查1*6的框 长连
def check_long(arr):
    blank=np.where(arr==0)
    black=np.where(arr==1)
    if len(blank[0])==1 and len(black[0])==5:
        return 1
    return 0

# check 1*5 square, one blank and three black apart from current location--four in a row
def check_4(arr):
    blank=np.where(arr==0)
    black=np.where(arr==1)
    if len(black[0])==4:
        return 2
    if len(blank[0])==2 and len(black[0])==3:
        return 1
    return 0

# check 1*4 square, one blank and two black apart from current location--three in a row
# Also must has two blank location on two sides.
def check_3_direct1(arr,i,j,whole_board,width):
    # any side not blank -> not 3
    if j==0 or j==width-4:
        return 0
    if (j>0 and whole_board[i][j-1]!=0) or (j+4<width and whole_board[i][j+4]!=0):
        return 0
    blank=np.where(arr==0)
    black=np.where(arr==1)
    if len(blank[0])==2 and len(black[0])==2:
        return 1
    return 0
def check_3_direct2(arr,i,j,whole_board,width):
    # any side not blank -> not 3
    if i==0 or i==width-4:
        return 0
    if (i>0 and whole_board[i-1][j]!=0) or (i+4<width and whole_board[i+4][j]!=0):
        return 0
    blank=np.where(arr==0)
    black=np.where(arr==1)
    if len(blank[0])==2 and len(black[0])==2:
        return 1
    return 0

def check_3_direct3(arr,i,j,whole_board,width):
    # any side not blank -> not 3
    if i==width-1 or j==0 or j==width-4 or i-3==0 or whole_board[i+1][j-1]!=0 or whole_board[i-4][j+4]!=0:
        # print('here')
        return 0
    blank=np.where(arr==0)
    black=np.where(arr==1)
    if len(blank[0])==2 and len(black[0])==2:
        return 1
    return 0

def check_3_direct4(arr,i,j,whole_board,width):
    # any side not blank -> not 3
    if i==0 or j==0 or j==width-4 or i==width-4 or whole_board[i-1][j-1]!=0 or whole_board[i+4][j+4]!=0:
        # print('here')
        return 0
    blank=np.where(arr==0)
    black=np.where(arr==1)
    if len(blank[0])==2 and len(black[0])==2:
        return 1
    return 0

# return 1 if x,y is forbiddened position
def forbidden_move(curPlayer,noncurPlayer,x,y,width):
    # if x==3 and y==3:
        # print(curPlayer,noncurPlayer)
    whole_board=np.copy(curPlayer)
    for i in range(width):
        noncur=np.where(np.array(noncurPlayer[i])==1)
        for j in noncur[0]:
            whole_board[i][j]=-1
    # for i in range(width):
    #     print(whole_board[i])
    cnt3=0
    cnt4=0
    cnt_long=0

    #### Direction1 vertical --- #######
    # 44: xooo?   xoo?o   _oo?o
    leftmost=max(y-4,0)
    rightmost=min(y+1,width-4)
    for j in range(leftmost,rightmost):
        # length 5 window
        # arr=[(x,k) for k in range(j,j+5)]
        # print(len(arr))
        arr=whole_board[x][j:j+5]
        # print(arr)
        flag4=check_4(np.array(arr))
        if flag4==2 and (j>0 and whole_board[x][j-1]!=1) and (j+5<width and whole_board[x][j+5]!=1):
            # print('1aa')
            return 0 # win
        if flag4==1:
            cnt4+=1
            break
    # 33:
    leftmost=max(y-3,0)
    rightmost=min(y+1,width-3)
    for j in range(leftmost,rightmost):
        # length 4 window
        arr=whole_board[x][j:j+4]
        # print(arr)
        if check_3_direct1(np.array(arr),x,j,whole_board,width)==1:
            cnt3+=1
            break
    # long
    leftmost=max(y-5,0)
    rightmost=min(y+1,width-5)
    for j in range(leftmost,rightmost):
        # length 4 window
        arr=whole_board[x][j:j+6]
        # print(arr)
        if check_long(np.array(arr))==1:
            cnt_long+=1
            break

    #### Direction2 horizontal | #######
    # 44:
    leftmost=max(x-4,0)
    rightmost=min(x+1,width-4)
    for j in range(leftmost,rightmost):
        # length 5 window
        arr=[]
        for k in range(j,j+5):
            arr.append(whole_board[k][y])
        # print(arr)
        flag4=check_4(np.array(arr))
        if flag4==2 and (j>0 and whole_board[j-1][y]!=1) and (j+5<width and whole_board[j+5][y]!=1):
            # print(arr)
            # print(np.where(np.array(arr)==1))
            # print('2aa')
            return 0 # win
        if flag4==1:
            cnt4+=1
            break
    # 33:
    leftmost=max(x-3,0)
    rightmost=min(x+1,width-3)
    for j in range(leftmost,rightmost):
        # length 4 window
        arr=[]
        for k in range(j,j+4):
            arr.append(whole_board[k][y])
        # if check_3_direct2(np.array(arr),x,j,whole_board,width)==1:
        if check_3_direct2(np.array(arr),j,y,whole_board,width)==1:
            cnt3+=1
            break

    # long
    leftmost=max(x-5,0)
    rightmost=min(x+1,width-5)
    for j in range(leftmost,rightmost):
        # length 4 window
        arr=[]
        for k in range(j,j+6):
            arr.append(whole_board[k][y])
        # print(arr)
        if check_long(np.array(arr))==1:
            cnt_long+=1
            break

    #### Direction3 upslope / #######
    # 44:
    if x+y>=4 and x+y<=10:
        tmp=min(7-x,y)
        # print(tmp)
        leftmost=min(tmp,4)
        tmp=min(x,7-y)
        rightmost=max(-4,-tmp)+3
        for j in range(leftmost,rightmost,-1):
            # length 5 window
            arr=[]
            for k in range(j,j-5,-1):
                arr.append(whole_board[x+k][y-k])
            # print(arr)
            flag4=check_4(np.array(arr))
            if flag4==2:
                if (x+j==width-1 or y-j==0 or (x+j+1<width and y-j>0 and whole_board[x+j+1][y-j-1]!=1)) and \
                   (y-j==width-5 or x+j-4==0 or (x+j-5>=0 and y-j+5<width and whole_board[x+j-5][y-j+5]!=1)):
                # print('3aa')
                    return 0 # win
            if flag4==1:
                cnt4+=1
                break
    # 33:
    if x+y>=3 and x+y<=11:
        tmp=min(7-x,y)
        leftmost=min(tmp,3)
        tmp=min(x,7-y)
        rightmost=max(-3,-tmp)+2
        for j in range(leftmost,rightmost,-1):
            # length 4 window
            arr=[]
            # print(j)
            for k in range(j,j-4,-1):
                arr.append(whole_board[x+k][y-k])
            if check_3_direct3(np.array(arr),x+j,y-j,whole_board,width)==1:
                cnt3+=1
                break
    #long
    if x+y>=5 and x+y<=9:
        tmp=min(7-x,y)
        leftmost=min(tmp,5)
        tmp=min(x,7-y)
        rightmost=max(-5,-tmp)+4
        for j in range(leftmost,rightmost,-1):
            # length 4 window
            arr=[]
            for k in range(j,j-6,-1):
                arr.append(whole_board[x+k][y-k])
            # print(arr)
            if check_long(np.array(arr))==1:
                cnt_long+=1
                break
    
    #### Direction4 downslope \ #######
    if x-y<=3 and x-y>=-3:
        tmp=min(x,y)
        # print(tmp)
        leftmost=min(tmp,4)
        leftmost=-leftmost
        tmp=width-max(x,y)-1
        rightmost=min(tmp,4)-3
        for j in range(leftmost,rightmost):
            # print(j)
            # length 5 window
            arr=[]
            for k in range(j,j+5):
                arr.append(whole_board[x+k][y+k])
            # if x==4 and y==3
            # print(arr)
            flag4=check_4(np.array(arr))
            if flag4==2:
                if(x+j==0 or y+j==0 or (x+j>0 and y+j>0 and whole_board[x+j-1][y+j-1]!=1)) and \
                   (x+j+4==width-1 or x+j+4==width-1 or (x+j+5<width and y+j+5<width and whole_board[x+j+5][y+j+5]!=1)):
                   
                   
                    # and whole_board[x+j-1][y+j-1]!=1 and whole_board[x+j+5][y+j+5]!=1:
                # print('4aa')
                    return 0 # win
            if flag4==1:
                cnt4+=1
                break

    # 33:
    if x-y<=4 and x-y>=-4:
        tmp=min(x,y)
        # print(tmp)
        leftmost=min(tmp,3)
        leftmost=-leftmost
        tmp=width-max(x,y)-1
        rightmost=min(tmp,3)-2
        for j in range(leftmost,rightmost):
            # length 4 window
            arr=[]
            # print(j)
            for k in range(j,j+4):
                arr.append(whole_board[x+k][y+k])
            # print(arr)
            if check_3_direct4(np.array(arr),x+j,y+j,whole_board,width)==1:
                cnt3+=1
                break

    #long
    if x-y<=2 and x-y>=-2:
        tmp=min(x,y)
        leftmost=min(tmp,5)
        leftmost=-leftmost
        tmp=width-max(x,y)-1
        rightmost=min(tmp,5)-4
        for j in range(leftmost,rightmost):
            # length 4 window
            arr=[]
            # print(j)
            for k in range(j,j+6):
                arr.append(whole_board[x+k][y+k])
            # print(arr)
            if check_long(np.array(arr))==1:
                cnt_long+=1
                break
    
    # print('cnt4',cnt4)
    # print('cnt3',cnt3)
    # print('cnt_long',cnt_long)
    if cnt4>=2 or cnt3>=2 or cnt_long>=1:
        # print('FORBIDDEN')
        return 1
    return 0

#Debug
# flag=forbidden_move(curPlayer,noncurPlayer,3,3,8)
# flag=forbidden_move(curPlayer,noncurPlayer,4,4,8)
# flag=forbidden_move(curPlayer,noncurPlayer,2,1,8)
# flag=forbidden_move(curPlayer,noncurPlayer,3,3,8) #33


# lastMove=last_move
# for i in range(8):
#     lastpos=np.where(np.array(lastMove[i])==1)
#     if len(lastpos[0])!=0:
#         x,y=i,lastpos[0][0]
# print(x,y)
# modi_curPlayer=curPlayer[:]
# modi_curPlayer[x][y]=0
# flag=forbidden_move(modi_curPlayer,noncurPlayer,x,y,8)
# if flag==1:
#     print('is forbidden')
# else:
#     print('not f')

# Qplayer
def cal_features(player,board,sensible_moves,thisplayerState,otherplayerState):
    # print(res.contblack2)
    # print(res.contblack3)
    for move in range(board.width * board.height):
        if move in sensible_moves:      
            for d in [1,7,8,9]:
                black = 0
                cnt = 1
                while ((move + d*cnt) in thisplayerState):
                    black += 1
                    cnt += 1
                cnt = 1
                while ((move - d*cnt) in thisplayerState):
                    black += 1
                    cnt += 1
                if black==1:
                    player.contblack2[move]=1
                elif black==2:
                    player.contblack3[move]=1
                elif black==3:
                    player.contblack4[move]=1
                elif black==4:
                    player.contblack5[move]=1
    for move in range(board.width * board.height):
        if move in sensible_moves:      
            for d in [1,7,8,9]:
                white = 0
                cnt = 1
                while ((move + d*cnt) in otherplayerState):
                    white += 1
                    cnt += 1
                cnt = 1
                while ((move - d*cnt) in otherplayerState):
                    white += 1
                    cnt += 1
                if white==2:
                    player.contwhite3[move]=1
                elif white==3:
                    player.contwhite4[move]=1
                elif white==4:
                    player.contwhite5[move]=1
    # return player
