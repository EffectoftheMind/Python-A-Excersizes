# Create a mapping of state to abbreviation
# Add Oklahoma and Texas to the end of the list.
states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI',
          'Oklahoma': 'OK',
          'Texas': 'TX'}
          
cities = {'CA': 'San Francisco',
          'MI': 'Detroit', 
          'FL': 'Jacksonville'}  
          
#add the rest of the cities here including Oklahoma and Texas

cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'
cities ['OK'] = 'Oklahoma City'
cities ['TX'] = 'Austin'

# Print out all the cities

print ("NY State has: ", cities['NY'])
print (cities)

# Print out all the states

print ("Michigan's abbreviation is: ", states['Michigan'])
print (states)
