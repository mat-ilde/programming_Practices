
"""
In this case I was not sure whether create a function was necessary, because the value tha will be change
was very specific. But if we need change value in other json file could be pretty easy using the function,
we just need to know our key like in the next program. For this reason I think the functions are always a good choice.
"""

import json

def getNewJson(json_file):
    #open the json file as reading
    with open(json_file, 'r') as fcc_file:
        #using load to convert json string to dict
        fcc_data = json.load(fcc_file)
    # id value=name value
    fcc_data["id"]= fcc_data["name"]
    #deleting the name key and value
    del fcc_data["name"]
    #formating to pretty string format using load
    final_json_file=json.dumps(fcc_data, indent=4)
    print(final_json_file)
    return final_json_file

if __name__ == '__main__':

    #calling the function with the json parameter
    getNewJson('/home/mati/Escritorio/one.json')