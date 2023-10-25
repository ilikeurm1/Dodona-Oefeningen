# https://dodona.be/nl/courses/107/series/1244/activities/1370867069

Weight = float(input('Geef je gewicht in (kg): '))
planetsNames = ['de maan', 'Venus', 'Jupiter', 'Mars', 'Neptunus' ]
planetsWeightFactors = [0.166, 0.9, 2.36, 0.37, 1.12 ]


Planet = str(input('Op welk hemellichaam ben je?: '))
try:
    chosenPlanet=planetsNames.index(Planet)
    print('Op', Planet, 'weeg je', Weight*planetsWeightFactors[chosenPlanet],'kilogram.')
except ValueError:
        print('Ongeldige invoer!')
