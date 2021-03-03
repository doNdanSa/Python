import random

money = 100

#Write your game of chance functions here
def fifty_fifty(amount, bet):

	if amount > 0 and amount <= money:
		print("Obstawiasz za {amount}.".format(amount = amount))
		if (bet.upper() == "HEADS" and random.randint(1,101) < 50) or (bet.upper() == "TAILS" and random.randint(1,101) > 50):
			cash = money + amount
			print("Wygrałeś! {amount} zostaje dodane do Twojego konta i wynosi {cash}!".format(amount = amount, cash = cash))
		else:
			cash = money - amount
			print('Niestety. Z Twojego konta ubywa {amount} i wynosi {cash}.'.format(amount = amount, cash = cash))
		return cash
	else: 
		print("Nie masz wystarczająco środków, aby obstawić za taką ilość.")


def Cho_Han(amount, bet):
	dice_1 = random.randint(1,6)
	dice_2 = random.randint(1,6)

	if amount >0 and amount <= money:
		if  (((dice_2 + dice_1) % 2 == 0  and bet.upper() == 'EVEN') or ((dice_2 + dice_1) % 2 != 0  and bet.upper() == 'ODD') ):
			cash_2 = money + amount
			print("Wygrałeś! {amount} zostaje dodane do Twojego konta i wynosi {cash}!".format(amount = amount, cash = cash_2))
		else:
			cash_2 = money - amount
			print('Niestety. Z Twojego konta ubywa {amount} i wynosi {cash}.'.format(amount = amount, cash = cash_2))
		return cash_2
	else: 
		print("Nie masz wystarczająco środków, aby obstawić za taką ilość.")

def higehst_card(p1_bet):
	p1_card = random.randint(1,13)
	p2_card = random.randint(1,13)

	if p1_bet > 0 and p1_bet <= money:
		if (p1_card > p2_card):
			cash_3 = money + p1_bet
			print("Wygrałeś i zarobiłeś {p1_bet}!".format(p1_bet=p1_bet))
		elif (p1_card < p2_card):
			cash_3 = money - p1_bet
			print("Niestety z Twojego konta ubywa {p1_bet}.".format(p1_bet = p1_bet))
		else:
			cash_3 = money
			print('Remis! Twoja kasa wraca do Ciebie.')
		return cash_3
	else: 
		print('Nie masz tyle kasy.')

def roulette(amount, bet):
	draw = random.randint(0,36)

	if amount > 0 and amount <= money:
		if draw == 0 and bet == "0":
			cash_4 = money + (amount * 37)
			print("Ty szczęśliwcu! Zgarniasz mocno powiększony bet! Masz {money}".format(money = cash_4))
		elif ((draw % 2 == 0 and bet.upper() == "ODD" ) or (draw % 2 != 0 and bet.upper() == "EVEN")):
			cash_4 = money + amount
			print('Los Ci sprzyja. Zgarniasz {amount} i masz {money}'.format(amount = amount, money = cash_4))
		else:
			cash_4 = money - amount
			print('Tracisz swój zakład. Zostało Ci {money}'.format(money = cash_4))
		return cash_4
	else:
		print('Nie masz tyle kasy.')







#Call your game of chance functions here

money = roulette(10, 'odd')
money = roulette(20, 'even')
money = roulette(40, '0')
money = roulette(20, 'odd')
money = roulette(10, 'even')

# money = fifty_fifty(25, 'tails')
# money = fifty_fifty(15, 'tails')
# money = fifty_fifty(5, 'heads')
# money = fifty_fifty(10, 'heads')
# money = fifty_fifty(10, 'tails')

# money = Cho_Han(7, 'even')
# money = Cho_Han(7, 'even')
# money = Cho_Han(7, 'odd')
# money = Cho_Han(7, 'odd')
# money = Cho_Han(7, 'even')
# money = Cho_Han(7, 'odd')

# money = higehst_card(20)
# money = higehst_card(10)
# money = higehst_card(15)
# money = higehst_card(10)
# money = higehst_card(20)
# money = higehst_card(10)