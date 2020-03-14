print('Account moved to Github 2807658845@qq.com or contact author by qq2807658845')
print('This version is  release on Github')
input('Press \'Enter\'to waste your money')
money = 100000
list = ['1.Hosts Protect-cost 430',
        '2. Pycharm Profession Useless-cost 7500',
        '3.Thanks Giving-cost 10400'
]
costs = [
        430,
        7500,
        10400,
]

for s in list:
        print(s)
while True:
        command = input()
        if money > 430:
                if command == '1':
                        money -= 430
                        print('Success')
                        print('Money in left', money)
                elif command == '2':
                        money -= 7500
                        print('Success')
                        print('Money in left', money)
                elif command == '3':
                        money -= 10400
                        print('Success')
                        print('Money in left', money)
                elif command == 'help':
                    print('It\'s easy, type the number of list to waste your money')

                else:
                        print('No such command')

        else:
                print('No enough money')