money = 1260
credit_list = [500, 100, 50, 10]

credit_cnt = 0

for credit in credit_list:
    give_money = (money // credit) * credit
    credit_cnt += (money // credit)
    money -= give_money

print(credit_cnt)