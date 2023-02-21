# Map
## About The Project
This module of functions should create a map.
The map that I created has three layers:
* The first one is the basic map. It only has one marker that indicates the starting location that the user enters from the command line.
* The second layer has only 10 markers: films which were made in the year that the user enters and were filmed nearest to latitude and longitude which should be entered from the command line. It also consists of another marker that indicates the starting location.
* The third layer. It happens that one film was shot for several years in different locations. So the third layer shows all the locations where one particular movie was shot.


## How to run the module?
To run this module the user should enter five arguments on the command line in that order:
1. year (for which you need to find movies)
2. latitude, longitude (coordinates of the starting point)
3. dataset (file with films)
4. film (for what film you need to find all locations where it was made)


## Example:
This is an example of how the module works:\
![image](https://user-images.githubusercontent.com/116542027/220388325-aef0838a-d0e3-4fa5-8918-89b1955b3196.png)

### The map with all three layers together:
![image](https://user-images.githubusercontent.com/116542027/220394879-a40d86b3-23c0-4c13-b417-e5132c52c51d.png)

![image](https://user-images.githubusercontent.com/116542027/220390030-1d8ca6b3-c186-4588-bb0a-13b0a0965c6a.png)

### The first layer (the basic one):

#### There is only one marker (the starting location)
![image](https://user-images.githubusercontent.com/116542027/220390936-291e56be-c6c7-4fd1-8538-0b844552059c.png)

### The second layer:
![image](https://user-images.githubusercontent.com/116542027/220392396-9047edc1-e667-43fd-abf2-9e9fa909e21b.png)

#### There are lots of markers that have almost the same location. But if you zoom in on the map, you can see the difference
![image](https://user-images.githubusercontent.com/116542027/220392959-36a12aa3-d302-4a33-a11e-eec1b2970b7d.png)

### The third layer:
#### The one film in different locations
![image](https://user-images.githubusercontent.com/116542027/220393745-40b9897d-119d-493c-8dd6-8891f7567f0a.png)

![image](https://user-images.githubusercontent.com/116542027/220393981-77410268-c2c8-44f6-9bf2-9c2eecb90f68.png)


### Built With
To create this module I used lots of modules such as:
* argparse
* geopy (to determine coordinates)
* math (to determine the distances)
* folium (to form a map)
