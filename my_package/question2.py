# return an object which shows the count of each character in a array of character
def count(characters): 
    result = {}
    for character in characters:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1
    return result

# group_by_key: return an object which shows the summed up value of each key in a array of object with key and value
def group_by_key(objects): 
    result = {}
    for object in objects:
        key = object['key']
        value = object['value']
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result