import random
import math

class Pokemon():
	def __init__(self, name, type, level = 5):
		self.name = name
		self.level = level
		self.type = type
		self.max_health = 100 + (23 * level )/10
		self.current_health = 100 + (23 * level )/10 
		self.knocked_out = False

	def __repr__(self):
		return 'Pokemon: {name}, has {current_health} health points remaining'.format(name = self.name, current_health=self.current_health)

	def knock_out(self):
		self.knocked_out = True
		if self.current_health != 0:
			self.current_health = 0
		print('Your Pokemon {name} was knocked out'.format(name = name))

	def lose_health(self, value):
		# Obliczanie otrzymanych obrażeń
		self.current_health -= value
		if self.current_health <= 0:
			self.current_health = 0
			self.knock_out
		else:
			print('{name} get {dmg} damage. Now has {current_health} hp!'.format(name = self.name, dmg = value, current_health = self.current_health))

	def gain_hp(self, value):
		# Przyrost hp
		self.current_health += value
		if self.current_health >= self.max_health:
			current_health = self.max_health
		print('{name} has now {current_health}'.format(name = self.name, current_health = self.current_health))

	def attack(self, opp_pokemon):
		# pseudolosowe obrażenia
		calc_dmg = math.ceil(self.level + (random.randint(0,100)/10))
		true_dmg = 0
		# czy jest wyrzucony
		if self.knock_out:
			print('{name} can\'t be used. {name} is knocked out!'.format(name = self.name))
				# zależności między typami
		if (self.type == 'Water' and opp_pokemon.type == 'Fire' or self.type == 'Fire' and opp_pokemon.type == 'Grass' or self.type == "Grass" and opp_pokemon.type == 'Water'):
			true_dmg = math.ceil(calc_dmg * (12/10))
			print('Your Pokemon\'s {my_name} attack agains {opp_name} was effective and dealt {dmg} dmg!'.format(my_name= self.name, opp_name = opp_pokemon.name, dmg=true_dmg))
			opp_pokemon.lose_health(true_dmg)
		if (self.type == 'Water' and opp_pokemon.type == 'Water' or self.type == 'Fire' and opp_pokemon.type == 'Fire' or self.type == "Grass" and opp_pokemon.type == 'Grass'):
			print('Your Pokemon\'s {my_name} attack agains {opp_name} dealt {dmg} dmg!'.format(my_name= self.name, opp_name = opp_pokemon.name, dmg=true_dmg))
			opp_pokemon.lose_health(calc_dmg)
		if (self.type == 'Fire' and opp_pokemon.type == 'Water' or self.type == 'Grass' and opp_pokemon.type == 'Fire' or self.type == "Water" and opp_pokemon.type == 'Grass'):
			true_dmg = math.ceil(calc_dmg * (8/10))
			print('Your Pokemon\'s {my_name} attack agains {opp_name} was less effective and dealt {dmg} dmg!'.format(my_name= self.name, opp_name = opp_pokemon.name, dmg=true_dmg))
			opp_pokemon.lose_health(true_dmg)


class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Arcanine(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Arcanine", "Fire", level)
        
class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Poliwrath(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Poliwrath", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)
        
class Chikorita(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Chikorita", "Grass", level)

class Trainer():
	def __init__(self,  name, pokemon_list, no_of_potion):
		self.name = name
		self.pokemons = pokemon_list
		self.potions = no_of_potion
		self.active_pokemon = 0

	def __repr__(self):
		print('The Trainer {name} has the following pokemons: '.format(name= self.name))
		for pokemon in self.pokemons:
			print (pokemon)
		return ('Following pokemon is {name}'.format(name = self.pokemons[self.active_pokemon].name))

	def change_active(self, new_pokemon):
		if new_pokemon >= 0 and new_pokemon <= (len(self.pokemons)):
			if self.pokemons[new_pokemon].knocked_out:
				print('You can\'t use {name}. Pokemon is knocked out!'.format(name = self.pokemons[new_pokemon].name))
			elif new_pokemon == self.active_pokemon:
				print('You can\'t use {name}. It\'s already active Pokemon!'.format(name = self.pokemons[new_pokemon].name))
			else:
				self.active_pokemon = new_pokemon
				print('You\'ve just selected {name}'.format(name = self.pokemons[self.active_pokemon].name))

	def use_potion(self):
		if self.potions > 0:
			print('You used potion on {name}'.format(name = self.pokemons[self.active_pokemon].name))
			self.pokemons[self.active_pokemon].gain_hp(30)
			self.potions -=1
		else:
			print('You have no potions left')

	def attack_opp(self,opponent):
		my_pokemon = self.pokemons[self.active_pokemon]
		op_pokemon = opponent.pokemons[opponent.active_pokemon]
		my_pokemon.attack(op_pokemon)


a = Charmander(7)
b = Arcanine(12)
c = Squirtle(18)
d = Bulbasaur(17)
e = Poliwrath(8)
f = Chikorita(11)

trainer_one = Trainer("Alex", [a,b,c], 3)
trainer_two = Trainer("Sara", [d,e,f], 5,)

print(trainer_one)
print(trainer_two)

trainer_one.attack_opp(trainer_two)
trainer_two.attack_opp(trainer_one)
trainer_two.use_potion()
trainer_one.attack_opp(trainer_two)
trainer_two.change_active(2)
trainer_two.change_active(1)
