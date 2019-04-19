## fails after the second time ##
import sys

file_name = 'recipes.txt'

try:
    with open(file_name, 'x') as my_file:
        my_file.write('Meatballs\n') ## append b'Meatballs' for byte and fail for unable to write case ##

except FileExistsError as err:## works like elif for particular error cases; as err is not mandatory##
    print(f"The {file_name} already exists")
    sys.exit(1) ## exit with non-zero exit status ##

except:
    print(f"Unable to write to {file_name}")
    sys.exit(1)

else:
    print(f"Wrote to {file_name}")

## always runs ##
finally:
    print(f"Execution completed")