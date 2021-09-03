import time

from find import find_documents
from getkeys import get_keys
from trapdoor import trapdoor

keyword_key, file_key, _ = get_keys('Tendium')
results = None
list_of_number_of_files = [10, 50, 100, 250, 500, 1000]
search_strings1 = [['date'], ['governments'], ['free'], ['date', 'governments'], ['date', 'free']]
search_strings2 = [['date'], ['thanksgiving'], ['please'], ['date', 'thanksgiving'], ['date', 'please']]
search_strings3 = [['date'], ['disney'], ['enron'], ['date', 'disney'], ['date', 'enron']]
search_strings4 = [['date'], ['dominating'], ['please'], ['date', 'dominating'], ['date', 'please']]
search_strings5 = [['date'], ['considerable'], ['please'], ['date', 'considerable'], ['date', 'please']]
search_strings6 = [['date'], ['surprises'], ['\\thomas_donohoe_dec2000\\notes'], ['date', 'surprises'],
                   ['date', '\\thomas_donohoe_dec2000\\notes']]
search_strings = [search_strings1, search_strings2, search_strings3, search_strings4, search_strings5, search_strings6]
collections = ['Tendium1', 'Tendium2', 'Tendium3', 'Tendium4', 'Tendium5', 'Tendium6']
for n in range(6):
    nr_of_files = list_of_number_of_files[n]
    search_queries = search_strings[n]
    print(f'Number of files: {nr_of_files}')
    print(f'Searched keywords: {search_queries}')
    for search_string in search_queries:
        timers = []
        for x in range(1000000):
            t0 = time.time()
            encrypted_keywords = []
            for keyword in search_string:
                encrypted_keywords.append(trapdoor(keyword_key, keyword))
            results = find_documents(collections[n], encrypted_keywords)
            t1 = time.time()
            timers.append(t1 - t0)

        print(f'Searched term is: {search_string}')
        print(f'Number of results: {len(results)}')
        print(f'Average search time is: {sum(timers) / len(timers)}')
        # print(f'Longest search time is: {max(timers)}')
        # print(f'Shortest search time is: {min(timers)}')
        print()
