## fails after the second time ##
import sys

file_name = 'recipes.txt'

try:
    with open(file_name, 'x') as my_file:
        my_file.write('Meatballs\n')

except:
    print(f"The {file_name} already exists")
    sys.exit(1) ## exit with non-zero exit status ##