# Analysis of companies and industries
Data consists of two files, one describing companies and the other describing industries.
The intention with this project is to analyze companies and update their industries.

The code extracts all key words from the industry data file and save them in a set. This set is put into a dictionary
with industry codes as keys.
Then, the code extracts data from each company's URL, and then matches the key words in the website with the key words
in each industry. An URL gets the industry code that has most word matching.

# Instructions to run the code
Run the code and it will print the urls for each company with an updated industry code and industry names.
Python 3.x