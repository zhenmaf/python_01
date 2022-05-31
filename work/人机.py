
import random

print('''
* * * * * * * * * *三英战吕布 * * * * * * * * *
              石头    剪刀     布
* * * * * * * * * * * * * * * * * * * * * * *
''')
player_name = input('请输入玩家姓名:')
print('1.刘备 2.关羽 3.张飞')
choice=eval(input('请选择电脑角色:'))

if choice==1:
    computer_name='刘备'
elif choice:
    cmputer_name = '关羽'
elif choice:
    cmputer_name = '关羽'
else:
    cmputer_name = '匿名'
print(player_name,'vs',computer_name)
while True:
    player_fist=eval(input('----------请出拳: 1.石头   2.剪刀   3.布----------\n'))
    if player_fist==1:
        player_fist_name='石头'
    elif player_fist==2:
        player_fist_name='剪刀'
    elif player_fist==3:
        player_fist_name='布'
    else:
        player_fist_name='石头'
        player_fist=1
    computer_fist=random(1,3)
    if computer_fist==1:
        computer_fist_name='石头'
    elif computer_fist==2:
        computer_fist_name='剪刀'
    else:
        computer_fist_name='布'
    print(player_name,'出拳:',player_fist_name)
    print(computer_name, '出拳:', computer_fist_name)
    if player_fist==computer_fist:
        print('平局')
    elif(player_fist==1 and computer_fist==2) or (player_fist==2 and computer_fist==3) or (player_fist==3 and computer_fist==1):
        print('玩家:',player_name,'胜')
    else:
        print('电脑: ',computer_name,'胜')
    answer=input('再来一局不?y/n')
    if answer !='y':
        break
