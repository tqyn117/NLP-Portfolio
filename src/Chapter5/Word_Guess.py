import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint
import pathlib
import sys


# Lexical_Diversity is done prior to any preprocessing as instructed
def lexical_diversity(tokens):
    set_tokens = set(tokens)
    print("Lexical diversity: %.2f" % (len(set_tokens) / len(tokens)))


def preprocessing(tokens):
    stop_words = set(stopwords.words('english'))
    # Lowercase, alpha only, not in stopword list, and length > 5
    tokens = [t.lower() for t in tokens if t.isalpha() if t not in stop_words if len(t) > 5]
    wnl = WordNetLemmatizer()
    # Get list of lemmas from tokens and then get unique lemmas
    lemmas = [wnl.lemmatize(t) for t in tokens]
    lemmas_unique = set(lemmas)
    # Perform POS tagging where we begin to separate nouns from other tags
    tags = nltk.pos_tag(lemmas_unique)
    print("First 20 tagged items: ", tags[:20])
    # Filter the list of lemmas with noun tags only (this includes NN, NNS, NNP, and NNPS)
    lemmas_noun = [t for t in tags if t[1] == "NN" or t[1] == "NNS" or t[1] == "NNP" or t[1] == "NNPS"]
    print("Num of tokens: ", len(tokens))
    print("Num of lemmas_noun: ", len(lemmas_noun))

    return tokens, lemmas_noun


def guessing_game(wordlist):
    seed(1234)
    score = 5
    word = wordlist[randint(0, 49)]
    board = '_' * len(word)
    # Start game
    print("Let's play a word guessing game!")
    while score >= 0:
        # If player guessed all the word's character continue onto the next word
        if '_' not in board:
            print("You solved it!\n")
            print("Current score: ", score, "\n")
            word = wordlist[randint(0, 49)]
            board = '_' * len(word)
            print("Guess another word")
        # Display the board of guesses and "_"
        print(' '.join(board))

        guess = input("Guess a letter:")
        # If player guessed a character that is in the word
        if guess in word:
            score += 1
            print("Right! Score is ", score)
            # Replaces "_" with correct character on guess board while removing
            #   from the word to ensure no duplicate guess
            for i in range(len(word)):
                if guess == word[i]:
                    word = word[:i] + '*' + word[i+1:]
                    board = board[:i] + guess + board[i+1:]
        # Exit the game loop if player input !
        elif guess == '!':
            break;
        # If player guessed a character that is not in the word and fail if score is below 0
        else:
            score -= 1
            if score < 0:
                print("Game over!")
            else:
                print("Sorry, guess again. Score is ", score)


if __name__ == '__main__':
    # Check if a filename is passed in as a system arg
    if len(sys.argv) < 2:
        print('Error: Missing system argument')
    else:
        fp = open(pathlib.Path.cwd().joinpath(sys.argv[1]), encoding='utf-8-sig', mode='r')
        raw_text = fp.read()
        tokens = word_tokenize(raw_text)

        lexical_diversity(tokens)

        tokens, nouns = preprocessing(tokens)

        # Using the tokens list and nouns list to create a dictionary of 50 nouns with the highest word count
        counts = {t[0]: tokens.count(t[0]) for t in nouns}
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        wordlist = sorted_counts[:50]
        wordlist = [n[0] for n in wordlist]

        guessing_game(wordlist)
