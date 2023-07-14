import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use.

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4= nlp("elephant")
word5 = nlp("cow")
word6 = nlp("tiger")

# Run the similarity check
print("cat" + " _ " + "monkey", word1.similarity(word2))
print("banana" + " _ " + "monkey", word3.similarity(word2))
print("banana" + " _ " + "cat", word3.similarity(word1))
print("elephant" + " _ " + "cow", word4.similarity(word5))
print("tiger" + " _ " + "cat", word6.similarity(word1))
print('------------------------------------------------------------------')
# Define a sentence to compare
sentence_to_compare = "why is my cat on the car"

sentences = [
    "Where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

# tokenise the sentence to compare
model_sentence = nlp(sentence_to_compare)

# We will now compare the similarity of the complaints to ascertain if spaCy's similarity
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " _ ", similarity)