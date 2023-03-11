password = 'a123456'
i = 2
while True:
    x = input('請輸入密碼(最多三次機會): ')
    if password != x and i > 0:
        print('密碼錯誤!', '還有' + str(i) + '次機會')
        int(i)
        i = i -1
    elif password != x and i == 0:
        print('解鎖失敗!')
        break
    elif password == x:
        print('登入成功')
        break