import re

file = './de_bello_gallico_3.txt'
# file_name = open(file)
# file_text = file_name.read()
output_file = open('output-3.txt', 'w')

# regex = re.compile('[\ ]')

with open(file) as f:
    with output_file as f1:
        for line in f:
            replaced = re.sub('\[?.\d?.\]', '', line)
            replaced2 = re.sub('\d', '', replaced)
            f1.write(replaced2)

# s = "Example String"
# replaced = re.sub('[ES]', 'a', s)
# print(replaced)

output_file.close()


# '\[?.\d?.\]'