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