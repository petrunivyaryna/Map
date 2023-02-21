"""
"""
import argparse
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
# from geopy.extra.rate_limiter import RateLimiter
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


def find_the_location(lst: list) -> list:
    """
    This function is created to find the latitude and longitude of the location using
    the element at the first index of list in lists of list. Then it should insert
    the tuple of latitude and longitude to the list at the second index.
    >>> find_the_location([['"15SecondScare"', 'Coventry, West Midlands, England, UK'], \
['"15SecondScare"', 'West Hills, California, USA'], ['"15SecondScare"', 'West Hills, \
California, USA'], ['"DearGeorgette"', 'New York City, New York, USA'], ['"KateConwayisaJerk"', \
'Toronto, Ontario, Canada'], ['"KateConwayisaJerk"', "Remark's Bar & Grill - 1026 Coxwell Ave, \
Toronto, Ontario, Canada"], ['"KateConwayisaJerk"', 'Gooderham Building, 49 Wellington \
Street East, Toronto, Ontario, Canada'], ['"KateConwayisaJerk"', "Russell Winkelaar's flat, \
Toronto, Ontario, Canada"], ['"KateConwayisaJerk"', 'Broadview Avenue, Toronto, Ontario, \
Canada'], ['"Millennials"', 'Los Angeles, California, USA'], ['"MommasGotBars"', 'Brooklyn, \
New York, USA'], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas Boulevard South, \
Las Vegas, Nevada, USA'], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas Boulevard \
South, Las Vegas, Nevada, USA'], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas \
Boulevard South, Las Vegas, Nevada, USA'], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las \
Vegas Boulevard South, Las Vegas, Nevada, USA']])
    [['"15SecondScare"', 'Coventry, West Midlands, England, UK', (52.4081812, \
-1.510477)], ['"15SecondScare"', 'West Hills, California, USA', (34.2032325, \
-118.645476)], ['"15SecondScare"', 'West Hills, California, USA', (34.3032325, \
-118.54547600000001)], ['"DearGeorgette"', 'New York City, New York, USA', (40.7127281, \
-74.0060152)], ['"KateConwayisaJerk"', 'Toronto, Ontario, Canada', (43.6534817, \
-79.3839347)], ['"KateConwayisaJerk"', "Remark's Bar & Grill - 1026 Coxwell Ave, \
Toronto, Ontario, Canada", (43.7534817, -79.2839347)], ['"KateConwayisaJerk"', \
'Gooderham Building, 49 Wellington Street East, Toronto, Ontario, Canada', \
(43.648366800000005, -79.37439532076982)], ['"KateConwayisaJerk"', "Russell Winkelaar's flat, \
Toronto, Ontario, Canada", (43.8534817, -79.18393470000001)], ['"KateConwayisaJerk"', 'Broadview \
Avenue, Toronto, Ontario, Canada', (43.6589555, -79.3498659)], ['"Millennials"', 'Los Angeles, \
California, USA', (34.0536909, -118.242766)], ['"MommasGotBars"', 'Brooklyn, New York, USA', \
(40.6526006, -73.9497211)], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas Boulevard \
South, Las Vegas, Nevada, USA', (36.1672559, -115.148516)], ['"$tripped"', 'Riviera Hotel & \
Casino - 2901 Las Vegas Boulevard South, Las Vegas, Nevada, USA', (36.2672559, -115.048516)], \
['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas Boulevard South, Las Vegas, Nevada, USA', \
(36.3672559, -114.94851600000001)], ['"$tripped"', 'Riviera Hotel & Casino - 2901 Las Vegas \
Boulevard South, Las Vegas, Nevada, USA', (36.467255900000005, -114.84851600000002)]]
    >>> find_the_location([['1 Single', 'Los Angeles, California, USA', 2006], ['1 Single', \
'New York City, New York, USA', 2006]])
    [['1 Single', 'Los Angeles, California, USA', (34.0536909, -118.242766), 2006], ['1 Single', \
'New York City, New York, USA', (40.7127281, -74.0060152), 2006]]
    """
    geolocator = Nominatim(user_agent = "MyProject")
    # geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    to_del = []
    for ind, films in enumerate(lst):
        try:
            location = geolocator.geocode(films[1])
            if location is None: # if geopy can't find the coordinates
                to_check = films[1].split(',')
                location = geolocator.geocode(",".join(to_check[1:]))
            films.insert(2, (location.latitude, location.longitude))
        except GeocoderUnavailable:
            to_del.append(ind)
    # delete elements from list if exception occurs
    i = 0
    for element in to_del:
        lst.pop(element - i)
        i += 1
    # checking if there are the same coordinates
    for sth in range(1, len(lst)):
        for previous in range(0, sth):
            if lst[sth][2] == lst[previous][2]:
                first = float(lst[sth][2][0]) + 0.1
                second = float(lst[sth][2][1]) + 0.1
                lst[sth][2] = tuple([first, second])
    return lst


films_for_year = input_from_file(dataset, int(year)) # read the file
film_in_different_locations = locations_for_film(dataset, film)
locations_for_film_in_year = find_the_location(films_for_year)
locations_for_one_film = find_the_location(film_in_different_locations)
print(locations_for_film_in_year)
print(locations_for_one_film)


print(films_for_year)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
