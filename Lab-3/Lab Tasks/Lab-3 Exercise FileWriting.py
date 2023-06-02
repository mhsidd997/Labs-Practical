with open('Cities.txt', 'w') as file:
    # Get the number of cities from the user
    num_cities = int(input("Enter the number of cities: "))
    
    # Loop through the cities
    for i in range(num_cities):
        # Get the data for each city
        name = input("Enter the name of city {}: ".format(i+1))
        population = input("Enter the population of city {}: ".format(i+1))
        mayor = input("Enter the name of the mayor of city {}: ".format(i+1))
        
        # Write the data to the file
        file.write("{},{},{}\n".format(name, population, mayor))

print("City data written to file.")