def get_city_year(p0, perc, delta, p):
    #Check if p is reachable from p0
    if p <= p0:
        return -1
    
    #initialize variables
    population = p0
    years = 0
    
    #Loop until the population reaches p or becomes less than p0
    while population < p:
        years += 1
        population = population + int(population * perc/100) + delta
        
        # If the population becomes less than p0, return -1
        if population < p0:
            return -1
    
    # Return the number of years when p is reached
    return years
#get_city_year (1000, 2, -50, 5000)
#get_city_year (1500, 5, 100, 5000) 
get_city_year(1500000, 2.5, 10000, 2_000_000)
print(get_city_year(1500000, 2.5, 10000, 2_000_000))