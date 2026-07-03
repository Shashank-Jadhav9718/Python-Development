# Write a function that takes a list of Python dictionaries and exports them into a perfectly formatted .csv file. You must manually handle the headers and safely escape any data that contains commas.


export_data = [
    {"Name": "Alice", "Age": 32, "City": "New York"},
    {"Name": "Bob", "Age": 45, "City": "San Francisco, CA"},
    {"Name": "Charlie", "Age": 28, "City": "Austin"}
]


file_name  = 'data.csv'

def export_to_csv(data , file_name):
    header = list(export_data[0].keys())
    with open(file_name , 'w') as file:
        header_row = ','.join(header)
        file.write(header_row + '\n')  
        
        for item in data:
            clean_v = []
            for key in header:
                value = str(item[key])
                if ',' in value:
                    value = f'"{value}"'
                
                clean_v.append(value)
                
            row_string = ','.join(clean_v)
            file.write(row_string+'\n')
    print(f"Successfully exported {len(data)} rows to {file_name}!") 
    
    
    
    
if __name__ == "__main__":
    export_to_csv(export_data , file_name) 