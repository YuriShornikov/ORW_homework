with open('1.txt', 'rt', encoding='utf-8') as file:
    # count = 0
    # for line in file:
    #     file.readline()
    #     count += 1
    # print(count)
    # print(file)
    r = file.read()

    count = r.count('\n')
    
    # def lines_count(s):
    #     if not s:
    #         return 0
    #
    #     count = s.count('\n')
    #     if not s.endswith('\n'):
    #         count += 1
    #     return count
    #
    # lines_count(r)
    print(count)
    print(r)
