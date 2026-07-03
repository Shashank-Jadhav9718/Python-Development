# Write a script that takes a flat JSON-formatted string and manually parses it into a native Python dictionary. You cannot use the json or ast modules.

raw_json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

def parse_json(json_string):
    dictionary = {}
    clean_string = json_string.strip()
    pairs = clean_string.split(',')
    for pair in pairs:
        key , value = pair.split(':')
        clean_key = key.strip()
        clean_value = value.strip()
        
        final_key = clean_key.strip('"')
        
        if clean_value.startswith('"'):
            final_value = clean_value.strip('"')
        else:
            final_value = int(clean_value)
            
        dictionary[final_key] = final_value
    
    return dictionary

if __name__ == "__main__":
    print("--- Raw String ---")
    print(type(raw_json_string))
    print(raw_json_string)

    print("\n--- Parsed Dictionary ---")
    result = parse_json(raw_json_string)
    print(type(result))
    print(result)
    print("\nAlice's Age + 5 years:", result["age"] + 5)