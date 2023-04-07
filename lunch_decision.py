# Lunch Decision Maker
import random
import numpy as np

def lunch_decision(lunch_list, weights, last_week):
    # determine probability
    all_weights_array = np.array(list(weights.values()))
    weights_avg = np.average(all_weights_array, axis=0)

    # choose destination based on probability
    decision = last_week
    while decision == last_week:
        decision = random.choices(lunch_list, weights_avg, k=1)

    return decision

lunch = [
    "love burger", 
    "BK", 
    "cheba", 
    "lindy's", 
    "bison witches", 
    "opa's", 
    "Boca", 
    "Boxyard",
    "Urban Pita",
    "Barrio Brewery",
    "empire pizza"
    ]

last_week = "Barrio Brewery"

all_weights = {    
    "Salim": [5, 6, 8, 9, 6, 8, 5, 7, 8, 9, 5],
    "Mike": [7, 9, 9, 9, 8, 9, 6, 8, 7, 8, 5],
    "Lori": [2, 10, 10, 4, 4, 7, 7, 5, 6, 8, 7],
    "David": [1, 9, 8, 6, 7, 8, 6, 3, 6, 5, 5],
    "Chiresha": [8, 7, 7, 8, 0, 0, 8, 10, 0, 5, 5],
}

print(lunch_decision(lunch, all_weights, last_week))