# Import all the things
import sys
import string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Open and read the text file
try:
    with open("alice.txt", encoding="utf-8-sig") as file:
        raw_text = file.read()
except FileNotFoundError:
    print("Whoops! The file wasn't found!")
    print("Make sure it's in the same folder as this script.")
    sys.exit()

# Make everything lowercase
clean_text = raw_text.lower()

# Replace hyphens and em dashes with spaces
clean_text = clean_text.replace("-", " ")
clean_text = clean_text.replace("—", " ")

# Define extra punctuation to remove (e.g., curly quotes)
extra_punctuation = '“”‘’…'

# Remove punctuation marks such as commas and periods
for mark in string.punctuation + extra_punctuation:
    clean_text = clean_text.replace(mark, "")

# Split the text into a list of individual words
words = clean_text.split()

# Create a dictionary to count the occurrences of each word
word_counts = {}

# Store all the stop words
stop_words = set(stopwords.words("english"))

# Loop through the list of words
for word in words:
    # If the word is a stop word, don’t count it
    if word in stop_words:
        continue
    # Has the word already come up?
    if word in word_counts:
        # If so, increment its count
        word_counts[word] += 1
    else:
        # If not, add it to the dictionary with a count of 1
        word_counts[word] = 1

# Sort the dictionary by word count (highest first)
sorted_words = sorted(word_counts.items(), 
                      key=lambda item: item[1], 
                      reverse= True)

# Print the 10 most common words
print("The 10 most common words in the text are:")
for word, count in sorted_words[:10]:
    print(f"{word}: {count}")

# Get a list of unique words
unique_words = set(words)

# Sort the unique words by length (longest first)
longest_words = sorted(unique_words, key=len, reverse=True)

# Print the 10 longest words
print("Top 10 longest words:")
for word in longest_words[:10]:
    print(f"{word} is {len(word)} characters long.")

# Replace curly quotes with regular quotes
raw_text = raw_text.replace("“", '"').replace("”", '"')
raw_text = raw_text.replace("‘", "'").replace("’", "'")

# Break the text into sentences
sentences = sent_tokenize(raw_text)

# Determine the length of each sentence, in words
sentence_lengths = [len(word_tokenize(sentence)) for sentence in sentences]

# Now get some basic stats
total_sentences = len(sentences)
shortest_sentence = min(sentence_lengths)
longest_sentence = max(sentence_lengths)
average_sentence = sum(sentence_lengths) / total_sentences

# Display the results
print(f"Number of sentences: {total_sentences}")
print(f"Shortest sentence: {shortest_sentence} words")
print(f"Longest sentence: {longest_sentence} words")
print(f"Average length: {average_sentence:.2f} words")

# Plot the sentence lengths on a graph
plt.hist(sentence_lengths, bins=30, edgecolor='black')
plt.title("Sentence Lengths in Words")
plt.xlabel("Words per sentence")
plt.ylabel("Number of sentences")
plt.show()

# Get a reference to VADER
analyzer = SentimentIntensityAnalyzer()

# Run a sentiment analysis on the raw text
scores = analyzer.polarity_scores(raw_text)

# Print the sentiment scores
print("Sentiment scores:")
print(scores)