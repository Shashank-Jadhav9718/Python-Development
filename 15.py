# Write a program that searches through a local text file and replaces a target word with a replacement word, saving the result into a completely new file without loading the entire file into memory at once.

source_file = 'sample.txt'
destination_file = source_file + '.replaced'

target = input('Enter the Target String: ')
replacement = input('Enter the Replacement String:')

def replacement_function(source_file , destination_file , target , replacement):
    found = False
    with open(source_file , 'r') as file , open(destination_file , 'w') as Writer:
        for line in file:
            if target in line:
                found = True
                Writer.write(line.replace(target , replacement))
            else:
                Writer.write(line)

    if found:
        print(f'Replaced occurrence of {target} with {replacement} in {destination_file}')
    else:
        print(f'Target string {target} was not found in the file.')
                
replacement_function(source_file , destination_file , target , replacement)


