import emoji

def main():
    table1 = " + + +"
    table2 = " + + +"
    table3 = " + + +"
    print(table1)
    print(table2)
    print(table3)
    move = 1
    while move<10:
        if not move%2:
            s = "0"
            print("Ход второго игрока")
        else:
            s = "x"
            print("Ход первого игрока")
        row = int(input("Введите номер строки: " ))
        col = int(input("Введите номер столбца: " ))
        try:
            if row == 1 and table1[col*2-1] == "+":
                table1 = table1[:col*2-1] + s + table1[col*2:]
                move += 1
            if row == 2 and table2[col*2-1] == "+":
                table2 = table2[:col*2-1] + s + table2[col*2:]
                move += 1
            if row == 3 and table3[col*2-1] == "+":
                table3 = table3[:col*2-1] + s + table3[col*2:]
                move += 1
        except:
            print("Неверный ввод")
            continue
        print(table1)
        print(table2)
        print(table3)
        if table1[1] == table1[3] == table1[5] == s or table2[1] == table2[3] == table2[5] == s or table3[1] == table3[3] == table3[5] == s \
        or table1[1] == table2[1] == table3[1] == s or table1[3] == table2[3] == table3[3] == s or table1[5] == table2[5] == table3[5] == s \
        or table1[1] == table2[3] == table3[5] == s or table1[5] == table2[3] == table3[1] == s:
            move -= 1
            break
    print(emoji.emojize(' ИГРА ЗАКОНЧЕНА :thumbs_up:'))
    if move == 10: print(emoji.emojize('Победила дружба:handshake:'))
    else:
        if s == "x": print(emoji.emojize('Победил первый игрок:1st_place_medal:'))
        else: print(emoji.emojize('Победил второй игрок:1st_place_medal:'))

if __name__ == '__main__':
    main()