import re

txt_file = "sample_text.txt"
text = open(txt_file, "r").readlines()

words = [] #list of unique words
word_count = 0 #total word count
paragraph_count = 0
sentences_count = 0

for i in text:
    if len(i) > 5:
        paragraph_count += 1
        words_found = re.findall("[A-Z]?[a-z]+", i)
        print "Words in paragraph " + str(paragraph_count) + ": " + str(len(words_found))
        for word in words_found:
            if not word in words:
                words.append(word)
        sentences_found = re.findall("([.!?])", i)
        sentences_count += len(sentences_found)
        word_count += len(words_found)
        print "Sentences in paragraph " + str(paragraph_count) + ": " + str(len(sentences_found))

print "Total words: " + str(word_count)
print "Total unique words: " + str(len(words))
print "Paragraphs: " + str(paragraph_count)
print "Total sentences: " + str(sentences_count)
