## to avoid closing each time ##

with open('xmen.txt', 'w+t') as my_file: ## write + text mode ##
    my_file.write("Beast\n")
    my_file.write("Phoenix\n")
    my_file.writelines(["Cyclops\n", "Bishop\n", "Nightcrawler\n",])


with open('xmen.txt', 'r') as my_file:
    print(my_file.read())