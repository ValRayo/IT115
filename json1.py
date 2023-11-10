#Class Library
import json 

#sample data
data = {
    'name': 'Osvaldo Guzman',
    'age': 31,
    'city': 'Seattle, WA',
    'interests': ['Anime','Gym','Running'],
    'is_student': False
}


#Writing data to a JSON file
with open('data.json', 'w') as json_file:

    json.dump(data, json_file, indent=4) 

print('Data has been written to data.json')


#Reading from the JSON file
with open('data.json', 'r') as json_file:
    #Load the data
    loaded_data = json.load(json_file)

print('Data loaded from data.json')
print(loaded_data)


    #Modification to Json file created.
loaded_data['age'] = 22
loaded_data['interests'].append('music')


#Write the modification to Json file created. 
with open('data.json', 'w') as json_file: 
    json.dump(loaded_data, json_file, indent=4)

print('Modified data to the data.json file')