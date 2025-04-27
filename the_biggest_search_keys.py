def the_biggest_search_keys(*key):
    if len(key) != 0:
        result = ""
        longest_key = []
        longitude = 0
        for i in key:
            print(i)
            if len(i) > longitude:
                longest_key.clear()
                longest_key.append(i)
                longitude = len(i)
                print(longitude)
            elif len(i) == longitude:
                longest_key.append(i)
                print(longest_key)

        longest_key.sort()
        print(longest_key)
        for i in longest_key:
            result += "'"+i+"', "
        print(result)
        return result[:len(result)-2]
    else:
        return "''"