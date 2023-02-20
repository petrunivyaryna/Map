"""
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('year')
parser.add_argument('latitude')
parser.add_argument('longtitude')
parser.add_argument('dataset')
parser.add_argument('film')

args = parser.parse_args()

year = args.year
latitude = args.latitude
longtitude = args.longtitude
dataset = args.dataset
film = args.film

def input_from_file(path: str, needed_year: int) -> dict:
    """
    This function should parse the file and create a dictionary in which the key
    is the year when the movie was made, and the value is the list where the first
    element is the name of the film and the second one is the location where the
    film was made. Then the function should return the values of the dictionary
    by the key which is equal to year argument.
    >>> input_from_file('locations.list', 2015)
    [['"15SecondScare"', 'Coventry, West Midlands, England, UK'], ['"15SecondScare"', \
'West Hills, California, USA'], ['"15SecondScare"', 'West Hills, California, USA'], \
['"DearGeorgette"', 'New York City, New York, USA'], ['"KateConwayisaJerk"', 'Toronto, \
Ontario, Canada'], ['"KateConwayisaJerk"', "Remark's Bar & Grill - 1026 Coxwell Ave, \
Toronto, Ontario, Canada"], ['"KateConwayisaJerk"', 'Gooderham Building, 49 Wellington \
Street East, Toronto, Ontario, Canada'], ['"KateConwayisaJerk"', "Russell Winkelaar's \
flat, Toronto, Ontario, Canada"], ['"KateConwayisaJerk"', 'Broadview Avenue, Toronto, \
Ontario, Canada'], ['"Millennials"', 'Los Angeles, California, USA'], ['"MommasGotBars"', \
'Brooklyn, New York, USA'], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas \
Boulevard South, Las Vegas, Nevada, USA'], ['"$tripped"', 'Riviera Hotel & Casino - \
2901 Las Vegas Boulevard South, Las Vegas, Nevada, USA'], ['"$tripped"', 'Riviera \
Hotel & Casino - 2901 Las Vegas Boulevard South, Las Vegas, Nevada, USA'], ['"$tripped"', \
'Riviera Hotel & Casino - 2901 Las Vegas Boulevard South, Las Vegas, Nevada, USA']]
    """
    with open(path, encoding = 'utf-8', errors = 'ignore') as file:
        data = file.readline()
        # skipping the unnecessary lines in file
        while not data.startswith('LOCATIONS LIST'):
            data = file.readline()
        to_add = file.readlines() # necessary lines

        # creating a dictionary(key = year, value = [film, location])
        year_for_films = {}
        for line in to_add[1:]:
            year_ind = line.strip().split('\t')[0].index('(') # year always in brackets
            # checking if the year is not '????'
            if line.strip().split('\t')[0][year_ind + 1: year_ind + 5].isdigit():
                year_of_filming = int(line.strip().split('\t')[0][year_ind + 1: year_ind + 5])
            else:
                break
            find_film = line.strip().split('\t')[0][: year_ind - 1]
            if find_film[1] == '#':
                find_film = find_film.replace('#', '') # the name of film without '#'
            for element in line.strip().split('\t')[1:]: # finding the location
                if element != '':
                    location = element
                    break
            if year_of_filming not in year_for_films: # creating the key + value
                year_for_films[year_of_filming] = [[find_film, location]]
            else: # add value to already existing key
                year_for_films[year_of_filming].append([find_film, location])
        return year_for_films[needed_year]


def locations_for_film(path: str, film_to_find: str) -> list:
    """
    The second argument of this function is the name of the film. This function
    should return all places and years where and when the film was made. Based on the
    output of this function I would create the third layer in the map.
    >>> locations_for_film('locations.list', '1 Single')
    [['1 Single', 'Los Angeles, California, USA', 2006], ['1 Single', 'New York City, \
New York, USA', 2006]]
    """
    with open(path, encoding = 'utf-8', errors = 'ignore') as file:
        data = file.readline()
        # skipping the unnecessary lines in file
        while not data.startswith('LOCATIONS LIST'):
            data = file.readline()
        to_add = file.readlines() # necessary lines
        result = []
        for line in to_add[1:]:
            year_ind = line.strip().split('\t')[0].index('(') # year always in brackets
            # checking if the year is not '????'
            if line.strip().split('\t')[0][year_ind + 1: year_ind + 5].isdigit():
                year_of_filming = int(line.strip().split('\t')[0][year_ind + 1: year_ind + 5])
            else:
                break
            find_film = line.strip().split('\t')[0][: year_ind - 1]
            if find_film[1] == '#':
                find_film = find_film.replace('#', '') # the name of film without '#'
            for element in line.strip().split('\t')[1:]: # finding the location
                if element != '':
                    location = element
                    break
            if film_to_find[1:-1] in find_film:
                result.append([film_to_find, location, year_of_filming])
        return result


films_for_year = input_from_file(dataset, int(year))
film_in_different_locations = locations_for_film(dataset, film)

print(film_in_different_locations)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
