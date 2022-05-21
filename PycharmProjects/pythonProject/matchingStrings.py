"""def matchingStrings(strings, queries):
    string_values_dict =dict()
    not_matched=False
    matched = list(string_values_dict.values())
    for string_string in strings:
        for string_query in queries:
            if string_query not in string_values_dict: #and string_query == string_string:
                string_values_dict[string_query] = 0
            string_values_dict[string_query] = string_values_dict[string_query] + 1
            print(string_query, string_values_dict.items())
            #print(string_string)
            #matched.append(string_values_dict.values())
            #string_values_dict[string_string]=string_values_dict[string_string]+1
    print(matched)

    return matched"""


def matchingStrings(strings, queries):
    string_values_dict = dict()
    not_matched = False
    matched = list(string_values_dict.values())
    for string_string in strings:
        for string_query in queries:
            if string_query not in string_values_dict:
                not_matched = False
            not_matched = True
            if not_matched and string_query==string_string:
                string_values_dict[string_query] = string_values_dict[string_query] + 1
            if not_matched==False and string_query != string_string:
                string_values_dict[string_query]=0
            print(string_values_dict[string_query])

    return matched


if __name__ == '__main__':
    strings = ["acbd", "acbd"]
    queries = ["aaa", "acbd", "ab"]
    matchingStrings(strings, queries)
