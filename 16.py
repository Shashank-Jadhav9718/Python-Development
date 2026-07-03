# Build a script that scans a log file for a specific error keyword (e.g., "CRITICAL") and extracts the timestamp and message into a separate summary file.

source_file = 'server.log'
destination_file = 'summary.txt'
target = input('Enter the target keyword : ').upper().strip()

def summary_function(source_file , destination_file , target):
    matches = []
    with open(source_file , 'r') as reader:
        for line in reader:
            if target in line:
                matches.append(line.replace('[', '').replace(']', ' ').replace(target, '').strip())


    
    if matches:
        with open(destination_file , 'w') as writer:
            writer.write('\n'.join(matches))
        print(f"Summary for {target} is Extracted in the {destination_file}")
    else:
        print(f'Target {target} not Found ')



    

        
        
if __name__ == '__main__':
    summary_function(source_file , destination_file , target)