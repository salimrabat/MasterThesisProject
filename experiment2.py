import os
import time

from pymongo.collection import Collection

from build_index import build_index
from env_var import db, test_folder_path
from getkeys import get_keys

keyword_key, file_key, _ = get_keys('Tendium')
timers = []
nr_of_files = 1000
sum_words = 0
sum_dis_words = 0
test_list = [10, 50, 100, 250, 500, 1000]
collection_number = 0
for n in test_list:
    collection_number += 1
    counter = 0
    t1 = time.time()
    sum_words = 0
    sum_dis_words = 0
    for subdir, dirs, files in os.walk(test_folder_path):
        if counter >= n:
            break
        count = 0
        for file in files:
            if counter >= n:
                t2 = time.time()
                t = t2 - t1
                timers.append(t)
                break
            counter += 1
            count += 1
            path_file = os.path.join(subdir, file)
            try:
                with open(path_file, 'r') as test_file:
                    text = test_file.read()
                    file_name = file + str(count)
                    encrypted_keywords = build_index(text, keyword_key, 'Tendium'+str(collection_number), path_file)
            except UnicodeDecodeError as err:
                pass

collection1: Collection = db['Tendium1']
results1 = collection1.find({})
max1 = 0
most_frequent_words1 = []
least_frequent_words1 = []
middle_frequent_words1 = []
size1 = []
for x in results1:
    x_length = len(x.get('documents'))
    if x_length not in size1:
        size1.append(x_length)
    if x_length > max1:
        max1 = x_length
        most_frequent_words1 = [x.get('_id')]
    elif x_length == max1:
        most_frequent_words1.append(x.get('_id'))
    elif x_length == 1:
        least_frequent_words1.append(x.get('_id'))
    elif x_length == 5:
        middle_frequent_words1.append(x.get('_id'))


collection2: Collection = db['Tendium2']
results2 = collection2.find({})
max2 = 0
most_frequent_words2 = []
least_frequent_words2 = []
middle_frequent_words2 = []
size2 = []
for x in results2:
    x_length = len(x.get('documents'))
    if x_length not in size2:
        size2.append(x_length)
    if x_length > max2:
        max2 = x_length
        most_frequent_words2 = [x.get('_id')]
    elif x_length == max2:
        most_frequent_words2.append(x.get('_id'))
    elif x_length == 1:
        least_frequent_words2.append(x.get('_id'))
    elif x_length == 31:
        middle_frequent_words2.append(x.get('_id'))

collection3: Collection = db['Tendium3']
results3 = collection3.find({})
max3 = 0
most_frequent_words3 = []
least_frequent_words3 = []
middle_frequent_words3 = []
size3 = []
for x in results3:
    x_length = len(x.get('documents'))
    if x_length not in size3:
        size3.append(x_length)
    if x_length > max3:
        max3 = x_length
        most_frequent_words3 = [x.get('_id')]
    elif x_length == max3:
        most_frequent_words3.append(x.get('_id'))
    elif x_length == 1:
        least_frequent_words3.append(x.get('_id'))
    elif x_length == 61:
        middle_frequent_words3.append(x.get('_id'))


collection4: Collection = db['Tendium4']
results4 = collection4.find({})
max4 = 0
most_frequent_words4 = []
least_frequent_words4 = []
middle_frequent_words4 = []
size4 = []
for x in results4:
    x_length = len(x.get('documents'))
    if x_length not in size4:
        size4.append(x_length)
    if x_length > max4:
        max4 = x_length
        most_frequent_words4 = [x.get('_id')]
    elif x_length == max4:
        most_frequent_words4.append(x.get('_id'))
    elif x_length == 1:
        least_frequent_words4.append(x.get('_id'))
    elif x_length == 135:
        middle_frequent_words4.append(x.get('_id'))

collection5: Collection = db['Tendium5']
results5 = collection5.find({})
max5 = 0
most_frequent_words5 = []
least_frequent_words5 = []
middle_frequent_words5 = []
size5 = []
for x in results5:
    x_length = len(x.get('documents'))
    if x_length not in size5:
        size5.append(x_length)
    if x_length > max5:
        max5 = x_length
        most_frequent_words5 = [x.get('_id')]
    elif x_length == max5:
        most_frequent_words5.append(x.get('_id'))
    elif x_length == 1:
        least_frequent_words5.append(x.get('_id'))
    elif x_length == 266:
        middle_frequent_words5.append(x.get('_id'))


collection6: Collection = db['Tendium6']
results6 = collection6.find({})
max6 = 0
most_frequent_words6 = []
least_frequent_words6 = []
middle_frequent_words6 = []
size6 = []
for x in results6:
    x_length = len(x.get('documents'))
    if x_length not in size6:
        size6.append(x_length)
    if x_length > max6:
        max6 = x_length
        most_frequent_words6 = [x.get('_id')]
    elif x_length == max6:
        most_frequent_words6.append(x.get('_id'))
    elif x_length == 1:
        least_frequent_words6.append(x.get('_id'))
    elif x_length == 514:
        middle_frequent_words6.append(x.get('_id'))


# size1.sort()
# size2.sort()
# size3.sort()
# size4.sort()
# size5.sort()
# size6.sort()
#
# print(len(size1))
# print(size1)
# print(len(size2))
# print(size2)
# print(len(size3))
# print(size3)
# print(len(size4))
# print(size4)
# print(len(size5))
# print(size5)
# print(len(size6))
# print(size6)

# print(f'Most frequent word in 10 files: {most_frequent_words1}')
# print(f'Least frequent word in 10 files: {least_frequent_words1}')
# print(f'Mid frequent word in 10 files: {middle_frequent_words1}')
#
# print(f'Most frequent word in 50 files: {most_frequent_words2}')
# print(f'Least frequent word in 50 files: {least_frequent_words2}')
# print(f'Mid frequent word in 50 files: {middle_frequent_words2}')
#
# print(f'Most frequent word in 100 files: {most_frequent_words3}')
# print(f'Least frequent word in 100 files: {least_frequent_words3}')
# print(f'Mid frequent word in 100 files: {middle_frequent_words3}')
#
# print(f'Most frequent word in 250 files: {most_frequent_words4}')
# print(f'Least frequent word in 250 files: {least_frequent_words4}')
# print(f'Mid frequent word in 250 files: {middle_frequent_words4}')
#
# print(f'Most frequent word in 500 files: {most_frequent_words5}')
# print(f'Least frequent word in 500 files: {least_frequent_words5}')
# print(f'Mid frequent word in 500 files: {middle_frequent_words5}')
#
# print(f'Most frequent word in 1000 files: {most_frequent_words6}')
# print(f'Least frequent word in 1000 files: {least_frequent_words6}')
# print(f'Mid frequent word in 1000 files: {middle_frequent_words6}')


# print(f'Number of words in all of the files: {sum_words}')
# print(f'Number of distinct keywords in all of the files: {sum_dis_words}')
# print(f'The average execution time is: {sum(timers) / len(timers)}')
# print(f'Longest time: {max(timers)}')
# print(f'Shortest time: {min(timers)}')
# print(f'Times: {timers}')
# t2 = time.time()
# t = t2 - t1
# print(f'execution time is {t}')

