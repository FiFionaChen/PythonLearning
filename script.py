destinations = ["Paris, France", "Shanghai, China", "LosAngeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
	destination_index = destinations.index(destination) 	
	return destination_index

desResult = get_destination_index("LosAngeles, USA")
print(desResult)

def get_traveler_location(traveler):
	traveler_destination = traveler[1]
	traveler_destination_index = get_destination_index(traveler_destination)
	return traveler_destination_index

	
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
	
attractions = list()
for x in destinations:
	x = []
	attractions.append(x)


print(attractions)
print(len(attractions))


attractions_for_destination = list()
def add_attraction(destination,attraction):	
	try:
		destination_index = get_destination_index(destination)
		attractions[destination_index] = attraction
		attractions_for_destination.append(attraction) 
		return attractions[destination_index], attractions_for_destination
	except:
		return
 
add_attraction("LosAngeles, USA","['Venice Beach', ['beach']]")
print(attractions)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)
print(attractions_for_destination)


