with open('HW_5.2.txt') as file:
    content = file.readlines()
    print(f'В файле {len(content)} строк(и)')
    num_str = 1
    for line in content:
        num_words = len(line.split())
        print(f'В строке №{num_str} {num_words} слов')
        num_str += 1
