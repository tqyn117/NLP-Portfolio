By Quy Giang
 
## Overview of NLP
This [document](Overview_of_NLP.pdf) includes a one page introduction of NLP as well as my objective for taking this NLP course.

## Assignment 1: Text Processor
This [program](https://github.com/tqyn117/NLP-Portfolio/blob/main/src/Chapter1/Text_Processor.py) processes employee information list file formatted in the order of last, first, middle initial, id, and office phone to a standardized format by creating an object for each employee and corrections from the user running the program. The output is a list of employee information in standardized format.

In order to run it, you must pass in the filepath to the file to be processed as a command-line argument for sys.argv. For example, you can run the project on powershell by executing the following command: python.exe Text_Processor.py data/data.csv
Here, data/data.csv is the filepath to the file to be processed.

In my opinion, Python strengths include but not limited to its library support and simplicity for text processing. By simplicity, Python allows developer to focus less on syntax and the behavior of the language while focusing on solving the problem. However, since Python is an interpreted language, it is slow and not memory efficient which can be a big problem when performing text processing for a much larger file.

From this first assignment, I learned how to setup my first Python project. Additionally, I got to properly practice Python's syntax and behavior for the first time. Using regex served as a good review for me on how to regulate data format.

## Assignment 2: Exploring NLTK
Jupyter Notebook and Comments about my observations can be found in this [PDF](https://github.com/tqyn117/NLP-Portfolio/blob/main/src/Chapter3/Exploring_NLTK_Jupyter_Notebook.pdf).

## Assignment 3: Guessing Word Game
This [program](https://github.com/tqyn117/NLP-Portfolio/blob/main/src/Chapter5/Word_Guess.py) is a word guess game where the word is a noun pulled randomly from a list of 50 nouns processed from a given text. The player has 5 points starting out. Each correct guess increases the score by 1 point. Each wrong guess decreases the score by 1 point. If player has negative score or input "!", they can exit out of the game.

## Assignment 4: Exploring WordNet
Jupyter Notebook and Comments about my observations can be found in this [PDF](https://github.com/tqyn117/NLP-Portfolio/blob/main/src/Chapter7/WordNet.pdf).

