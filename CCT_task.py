#Author: Auksė Levonaitė
from typing import List
from array import *

def add_train_stations_to_cities(number_of_cities: int, cities_with_train_station: List[int]):
    #Initialize cities array with zeros
    cities = []
    cities = [0 for i in range(number_of_cities)] 
    
    #add 1 as sign to cities if train station is in the city
    for x in cities_with_train_station:
        cities[x] = 1
    return cities

def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
         
    #Create cities_with_train_station array
    cities_with_train_station = add_train_stations_to_cities(number_of_cities, cities_with_train_station) 

    #calculate maximum distance
    maxDistance = 0;
    previous = -1;
    size = number_of_cities;
    
    for x in range(0,size):
        if cities_with_train_station[x] == 0:
            continue;
        #if left of x is all empty (no train station in city) 
        if previous == -1:
            maxDistance = x       
        else:
            maxDistance = max(maxDistance, int((x - previous)/2))
        
        previous = x;          
        
    #if right end side is empty
    if cities_with_train_station[size-1] == 0:
        maxDistance = max(maxDistance, size - 1 - previous)
        
    return maxDistance;


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    assert (
        find_maximum_distance(number_of_cities=6, cities_with_train_station=[0, 3,5]) == 1
    )
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 3]) == 1
    )
    assert (
        find_maximum_distance(number_of_cities=10, cities_with_train_station=[0, 5,8]) == 2
    )
    print("ALL TESTS PASSED")