counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

print("----------Breakline1-----------")

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoes and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoes or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

print("----------Breakline2-----------")
  
for county in counties:
    print(county)

print("----------Breakline3-----------")

# use a for loop to iterate over a dictionary and get all the keys, all the values, or all the keys and values.
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# To get only the keys from a dictionary using a for loop.
for county in counties_dict:
    print(county)

# use the keys() method to iterate over a dictionary to get the keys.
for county in counties_dict.keys():
    print(county)

# iterate over the dictionary using the values() method.
for voters in counties_dict.values():
    print(voters)

# use the format dictionary_name[key] to get the value for the key.
print(counties_dict['Arapahoe'])
print(counties_dict['Denver'])
print(counties_dict['Jefferson'])

print("----------Breakline4-----------")
# using the format dictionary_name[key],return the value of the key in the output.
for county in counties_dict:
    print(counties_dict[county])

# get the values of a key is to use the get() method on the dictionary in the for loop
for county in counties_dict:
    print(counties_dict.get(county))

print("----------Breakline5----------")

# get the key and the value for each dictionary, output will be each key and value in order.
for county, voters in counties_dict.items():
    print(county, voters)

# Print each county and registered voter form the counties dictionary
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

print("----------Breakline6-----------")

# each dictionary is printed on a separate line
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

print("----------Breakline7-----------")    

# iterate over the list of dictionaries and print the counties in voting_data
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# retrieve each dictionary,the output is each value from each key
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("----------Breakline8-----------")  
# retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# only print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])
   
print("----------Breakline9-----------")  
print(voting_data[0].values())
print(voting_data[0].items())

# Print each county and registered voter from the dictionary   
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.") 

print("----------Breakline10-----------") 

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes *100:.2f} % of the total votes.")
print(message_to_candidate)



