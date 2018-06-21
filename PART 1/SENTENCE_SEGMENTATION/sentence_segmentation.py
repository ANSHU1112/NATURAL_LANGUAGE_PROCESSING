from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Priyanshu! How are you? My first paper is on Monday, and I am really happy."

print(sent_tokenize(example_text))  #sentence segmentation

print(word_tokenize(example_text))   #word by word segmentation

for i in word_tokenize(example_text):   #print all the segmenated word
    print(i)
