planets = {'de maan': 0.166, 'Venus': 0.9, 'Jupiter': 2.36, 'Mars': 0.37, 'Neptunus': 1.12}
Weight, Planet = float(input()), input()
try:
    print(f"Op {Planet} weeg je {Weight * planets[Planet]} kilogram.")
except ValueError:
        print('Ongeldige invoer!')

# Weight = float(input('Geef je gewicht in (kg): '))
# planetsNames = ['de maan', 'Venus', 'Jupiter', 'Mars', 'Neptunus' ]
# planetsWeightFactors = [0.166, 0.9, 2.36, 0.37, 1.12 ]
# Planet = str(input('Op welk hemellichaam ben je?: '))
# try:
#     chosenPlanet=planetsNames.index(Planet)
#     print(f"Op {Planet} weeg je {Weight * planetsWeightFactors[chosenPlanet]} kilogram.")
# except ValueError:
#         print('Ongeldige invoer!')
