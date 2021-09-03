import matplotlib.pyplot as plt

nr_of_files1 = 10
size1 = 91.9677734375
nr_of_words1 = 4163
nr_of_distinct_words1 = 1674
average_time1 = 0.9211216263771057
max_time1 = 1.271777629852295
min_time1 = 0.8269922733306885

nr_of_files2 = 50
size2 = 311.359375
nr_of_words2 = 19748
nr_of_distinct_words2 = 4705
average_time2 = 3.3962488312721253
max_time2 = 3.8309943675994873
min_time2 = 3.290412425994873

nr_of_files3 = 100
size3 = 580.47265625
nr_of_words3 = 39531
nr_of_distinct_words3 = 7861
average_time3 = 6.712013073444367
max_time3 = 7.253777027130127
min_time3 = 6.587518215179443

nr_of_files4 = 250
size4 = 1076.9150390625
nr_of_words4 = 90971
nr_of_distinct_words4 = 10465
average_time4 = 15.690115651845932
max_time4 = 16.46463918685913
min_time4 = 15.490975141525269

nr_of_files5 = 500
size5 = 1863.517578125
nr_of_words5 = 187889
nr_of_distinct_words5 = 12629
average_time5 = 33.23863577151298
max_time5 = 46.26535725593567
min_time5 = 32.05919814109802

nr_of_files6 = 1000
size6 = 3834.28515625
nr_of_words6 = 371538
nr_of_distinct_words6 = 24956
average_time6 = 65.13434722828865
max_time6 = 70.10951662063599
min_time6 = 64.32620644569397

fig1, ax1 = plt.subplots()
ax1.set(xlabel='Total number of words in files', ylabel='time (s)',
        title='Index Building Average Execution Time')
ax1.plot([nr_of_words1, nr_of_words2, nr_of_words3, nr_of_words4, nr_of_words5, nr_of_words6],
         [average_time1, average_time2, average_time3, average_time4, average_time5, average_time6], '-bo')
fig3, ax3 = plt.subplots()
ax3.set(xlabel='Number of files', ylabel='time (s)',
        title='Index Building Average Execution Time')
ax3.plot([nr_of_files1, nr_of_files2, nr_of_files3, nr_of_files4, nr_of_files5, nr_of_files6],
         [average_time1, average_time2, average_time3, average_time4, average_time5, average_time6], '-bo')
fig2, ax2 = plt.subplots()
ax2.set(xlabel='Number of distinct words in files', ylabel='size (Kilobytes)',
        title='Index Building Database Size')
ax2.plot(
    [nr_of_distinct_words1, nr_of_distinct_words2, nr_of_distinct_words3, nr_of_distinct_words4, nr_of_distinct_words5,
     nr_of_distinct_words6], [size1, size2, size3, size4, size5, size6], '-bo')

xs = [nr_of_files1, nr_of_files2, nr_of_files3, nr_of_files4, nr_of_files5, 750, nr_of_files6]
zs = [size1, size2, size3, size4, size5, 3228.1923828125, size6]
ys = [nr_of_distinct_words1, nr_of_distinct_words2, nr_of_distinct_words3, nr_of_distinct_words4, nr_of_distinct_words5,
      19769, nr_of_distinct_words6]
fig = plt.figure()
ax3 = fig.add_subplot(projection='3d')
ax3.set(xlabel='Number of files', ylabel='Number of distinct words in files', zlabel='size (Kilobytes)')
ax3.plot(xs, ys, zs, '-bo')

plt.show()
