from random import choice

city = "Iasi"

bird = "cucuvea"

flower = "trandafir"

song = "Trandafir de la Moldova"

def randomfunfact():
	funfacts = [
		"Iasi is the third largest city in Romania and the seat of Iași County",
		"Still referred to as The Moldavian Capital, Iași is the main economic and business centre of Romania's Moldavian region.",
		"Home to the oldest Romanian university and to the first engineering school, Iași is one of the most important education and research centres of the country, accommodating over 60,000 students in five public universities",
		"The city is also known as the site of the largest Romanian pilgrimage which takes place every year, in October",
	]
	index = choice("0123")
	print(funfacts[int(index)])
if __name__ == "__main__":
	randomfunfact()
