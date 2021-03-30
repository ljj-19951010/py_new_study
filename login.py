'''
 登录和注册系统
'''

import time

# 菜单界面
user_list = {}
def mean():
    print('''
        ===========Student Manage===========
         |***** 1.Login to the system *****|
         |***** 2.The system registry *****|
         |***** 3.Quit system         *****|
        ====================================
        ''')
    enter_input = int(input('Please select num(int):'))
    if enter_input == 1:
        print('**********Enter system**********')
        time.sleep(1)
        go()
    elif enter_input == 2:
        account_reg()
    elif enter_input == 3:
        print('*********QUIT SYSTEM**********')
    else:
        print('ERROR!!!')
        time.sleep(1)
        mean()

# 进度条界面
def go():
    for i in range(0,101):
        print("\r",end='')         # \r 表示将光标的位置回退到本行的开头位置
        print('{}%:'.format(i),'=' * (i // 2),end='')
        time.sleep(0.03)
    print('\n')
    account_lo()

# 注册
def account_reg():
    mark = True
    while mark:
        user_input = input('Please input your account:')
        pass_input = input('Please input your password:')
        user_list[user_input] = pass_input
        print('Successful!!\nYour account is:',user_list)
        continue_enter = input('Are you continue(y/n):')
        if continue_enter == 'y' or continue_enter == 'Y':
            mark = True
        elif continue_enter == 'n' or continue_enter == 'N':
            mark = False
            print('Login finally!GO to Mean!!')
            time.sleep(1)
            mean()
        else:
            print('ERROR!!!!!!!')

# 登录
def account_lo():
    enter_user = input('user:')
    enter_pass = input('passwords:')

    if enter_user in user_list.keys() and enter_pass in user_list[enter_user]:
        print('login successful')
    else:
        print('Login error,please try again!')
        mean()


if __name__ == '__main__':
    mean()
