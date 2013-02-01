from __future__ import division
import random
import sys
import math

# *butter*, *caster sugar*, *self-raising flour* & *eggs*

# Pool
pool = []

# Parents
parents = []

# Offspring
offspring = []

# Scoring
total_score = 0

def score(cake):
	score = abs(225 - cake[0])
	score = score + abs(225 - cake[1])
	score = score + abs(225 - cake[2])
	score = score + abs(4 - cake[3])
	
	if not cake[0] == cake[1] == cake[2]:
		score = score + 10

	return score

def fitness(cake):
	fitness = 1
	if cake[0] == 255:
		fitness += 1
	if cake[1] == 255:
		fitness += 1
	if cake[2] == 255:
		fitness += 1
	if cake[3] == 4:
		fitness += 1
	return int(math.exp(fitness))
	# return int((5 / fitness) * 100) *  int((5 / fitness) * 100)
	# return int(100 - ( score(cake) / total_score) * 100)
	
def bake(cake):
	# Mutate the amount of the ingredient around one time in a hundred
	for ingredient in range(len(cake)):
		if random.random() < 0.01:
			# The mixing bowl can only hold 10kg of any 1 ingredient
			cake[ingredient] = random.randint(1,1000)
			
	return cake
	
def calculate_total(population):
	internal_score = 0
	for i in range(len(population)):
		internal_score = internal_score + score(population[i])
	return internal_score

def make():
	cake = []
	for _ in range(4):
		cake.append(random.randint(1,1000))
	return cake
	
def mate(a, b):
	cake_jr = []
	midpoint = random.randint(0,4)
	for i in range(midpoint):
		cake_jr.append(a[i])
	for i in range(4 - midpoint):
		cake_jr.append(b[midpoint + i])
	return cake_jr
	
# Initialisation
for i in range(10):
	pool.append(make())
	
while True:
	total_score = calculate_total(pool)
	# Add the members of the population to the parents pool by probablility
	for i in range(len(pool)):
		for j in range(fitness(pool[i])):
			if fitness(pool[i]) == 148:
				print pool
				print "\n\n"
				print "Correct Member Found! \t"
				print pool[i]
				sys.exit()
			parents.append(pool[i])
	
	# Pick 10 random parents and mate them
	for times in range(50):
		offspring.append(bake(mate(random.choice(parents), random.choice(parents))))
			
	pool[:]=offspring
	del parents[:]
	del offspring[:]
	
	print pool
		
	