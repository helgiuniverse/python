# __________________________read_files______________________
text = open('/Users/oleg/IdeaProjects/Python/file.txt')
text_1 = text.read()
print(text_1)
for line in text:
    if 'real slim shady' in line:
        print(line, end='')
with open('/Users/oleg/IdeaProjects/Python/file.txt') as y:
    line = y.readline()
    while line:
        print(line, end='')
        line = y.readline()
text.close()
print('\n')
x = open('/Users/oleg/IdeaProjects/Python/file.txt')
x1 = x.readlines()
print(x1[2])
x.close()
# ________________write_files________________
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
with open('/Users/oleg/IdeaProjects/Python/rainbow_colors.txt', 'w') as rainbow_colors:
    for color in color_list:
        print(color, file=rainbow_colors)
new_color_list = []
# with open('/Users/oleg/IdeaProjects/Python/rainbow_colors.txt', 'r') as rainbow_colors:
#     for color in rainbow_colors:
#         new_color_list.append(color.strip('\n'))
# print(new_color_list)
list_of_another_colors = ['dark green', 'brown', 'white', 'black', 'gray']
with open('/Users/oleg/IdeaProjects/Python/rainbow_colors.txt', 'a') as rainbow_colors:
    for color in list_of_another_colors:
        print(color, file=rainbow_colors)
