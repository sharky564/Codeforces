money = int(input())
hundred = money // 100
money -= hundred * 100
twenty = money // 20
money -= twenty * 20
ten = money // 10
money -= ten * 10
five = money // 5
money -= five * 5
one = money

print(hundred + twenty + ten + five + one)
