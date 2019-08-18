with open('./hometask04/source_data.csv', 'r') as f:
    strings = f.readlines()

names = set()
cities = set()
for string in strings[1:]:
    values = string.split(',')
    names.add(values[0].strip())
    cities.add(values[1].strip())
names = list(names)
cities = list(cities)
yes_no = ['+', '-']

test_data = [(name, city, x, y, z) for name in names for city in cities for x in yes_no for y in yes_no for z in yes_no]
with open('./hometask04/test_data.txt', 'w', encoding='utf-8') as f:
    for line in test_data[:100]:
        f.writelines('	'.join(line) + '\n')
