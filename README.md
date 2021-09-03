# MasterThesisProject
Searchable Encryption Scheme

Steps:
1. Download the enron dataset from this link http://enrondata.org/en/latest/ and unzip it.
2. Change the test_folder_path variable in env_var.py to match the location of the dataset.
3. Run experiment2.py to create the multiple database collection that vary in the number of files they handled.
4. Run experiment3.py to query the words that were extracted from the logs of experiment2.py
5. Run plot_build_index.py to get the performance results graph for building an index database.
6. Run the plot_search.py to get the performance results graph for querying the index database.
