# BIO380
BIO380 data science project.

This data project focuses on data retrieved from non-voters in the /fivethirtyeight github repository. 

Per the repository's read-me the data was collected using the Ipsos Knowledge panel - “a probability-based online panel that is recruited to be representative of the U.S. population.” Non-voters were defined as individuals who never vote, or those who vote rarely (1 in 4 elections). 

The data is first sorted by the answersorter.sh file which when run will break up the data into multiple text files each corresponding to an individual qustion. Text files are appropriately named for the question which they hold the answers to. 
Following this sort, using the nonvoters_codebook.pdf provided by /fivethrityeight users can look across questions and find questions of interest which they want to analyze. 
Then using the pythonit.py file the user will be prompted to enter in the name of the question. The user can input any question eg. "Q3_4" and the pythonit.py file will create an output folder with the answers to that question presented in an organized and readable fashion. The output folder contains 3 files: an output.txt with the questions orgnaized by answer choice and portportion, an outbar.png file showing the answers as a bar graph, and an outpie.png file showing the answers as portportions in a pie chart.
