import matplotlib.pyplot as plt

nr_of_files1 = 10
single_most_word_avg_time1 = 0.00029226995086669924*1000
single_least_word_avg_time1 = 0.00028990043592453003*1000
single_mid_word_avg_time1 = 0.0002913681693077087*1000
multi_most_least_word_avg_time1 = 0.0005517433576583862*1000
multi_most_mid_word_avg_time1 = 0.0005539719367027283*1000

nr_of_files2 = 50
single_most_word_avg_time2 = 0.00029592105746269225*1000
single_least_word_avg_time2 = 0.00028930812191963194*1000
single_mid_word_avg_time2 = 0.0002948554582595825*1000
multi_most_least_word_avg_time2 = 0.0005606264894008636*1000
multi_most_mid_word_avg_time2 = 0.0005697014746665955*1000

nr_of_files3 = 100
single_most_word_avg_time3 = 0.0003012204160690308*1000
single_least_word_avg_time3 = 0.0002903077473640442*1000
single_mid_word_avg_time3 = 0.0002975981442928314*1000
multi_most_least_word_avg_time3 = 0.000568452151298523*1000
multi_most_mid_word_avg_time3 = 0.0005836329610347748*1000

nr_of_files4 = 250
single_most_word_avg_time4 = 0.0003126535439491272*1000
single_least_word_avg_time4 = 0.00028929979038238527*1000
single_mid_word_avg_time4 = 0.00030331987977027895*1000
multi_most_least_word_avg_time4 = 0.0005895105981826782*1000
multi_most_mid_word_avg_time4 = 0.0006190750544071197*1000

nr_of_files5 = 500
single_most_word_avg_time5 = 0.000335712370634079*1000
single_least_word_avg_time5 = 0.0002892003786563873*1000
single_mid_word_avg_time5 = 0.0003137866220474243*1000
multi_most_least_word_avg_time5 = 0.0006249892182350158*1000
multi_most_mid_word_avg_time5 = 0.0006853956515789032*1000

nr_of_files6 = 1000
single_most_word_avg_time6 = 0.0003720153057575226*1000
single_least_word_avg_time6 = 0.00029009138107299805*1000
single_mid_word_avg_time6 = 0.000336488596200943*1000
multi_most_least_word_avg_time6 = 0.0006915015914440155*1000
multi_most_mid_word_avg_time6 = 0.0008179742753505706*1000

x = [nr_of_files1, nr_of_files2, nr_of_files3, nr_of_files4, nr_of_files5, nr_of_files6]

# Single Keyword Search for most frequent word
y1 = [single_most_word_avg_time1, single_most_word_avg_time2, single_most_word_avg_time3, single_most_word_avg_time4,
      single_most_word_avg_time5, single_most_word_avg_time6]
plt.plot(x, y1, '-o', label="SKS-MostFW")
# Single Keyword Search for mid frequent word
y2 = [single_mid_word_avg_time1, single_mid_word_avg_time2, single_mid_word_avg_time3, single_mid_word_avg_time4,
      single_mid_word_avg_time5, single_mid_word_avg_time6]
plt.plot(x, y2, '-o', label="SKS-MidFW")
# Single Keyword Search for least frequent word
y3 = [single_least_word_avg_time1, single_least_word_avg_time2, single_least_word_avg_time3,
      single_least_word_avg_time4, single_least_word_avg_time5, single_least_word_avg_time6]
plt.plot(x, y3, '-o', label="SKS-LeastFW")
# Multi Keyword Search for most and least frequent word pair
y4 = [multi_most_least_word_avg_time1, multi_most_least_word_avg_time2, multi_most_least_word_avg_time3,
      multi_most_least_word_avg_time4, multi_most_least_word_avg_time5, multi_most_least_word_avg_time6]
plt.plot(x, y4, '-o', label="MKS-MLFWP")
# Multi Keyword Search for most and mid frequent word pair
y5 = [multi_most_mid_word_avg_time1, multi_most_mid_word_avg_time2, multi_most_mid_word_avg_time3,
      multi_most_mid_word_avg_time4, multi_most_mid_word_avg_time5, multi_most_mid_word_avg_time6]
plt.plot(x, y5, '-o', label="MKS-MMFWP")

plt.xlabel('Number of files')
# Set the y axis label of the current axis.
plt.ylabel('Time (ms)')
# Set a title of the current axes.
plt.title('Search Query Average Execution Time')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
