import nltk #6740035722 ชนวีร์ ภู่ตระกูล
from collections import Counter
class Concordancer:

    left_context_length = 50
    right_context_length = 50

    def __init__(self):
        self.sentence = []

    def read_tokens(self, file_name):
        with open(file_name) as file:
            for word in file:
                tokens = nltk.wordpunct_tokenize(word)
                self.sentence.append(tokens)

    def find_concordance(self, query, num_words):
        output = []
        for list in self.sentence:
            for i, word in enumerate(list):
                if word == query:
                    Left = list[max(0,i - num_words): i]
                    Right = list[i + 1: (i + 1) + num_words]
                    Left_text = ' '.join(Left)[-self.left_context_length:].rjust(self.left_context_length)
                    Right_text = ' '.join(Right)[:self.right_context_length].ljust(self.right_context_length)
                    new_line = f"{Left_text} {query} {Right_text}"
                    output.append(new_line)
        if output:
            for line in output:
                print(line)
        else:
            print('"Query not found…"')

    def find_concordance_ngram(self, ngram_query, num_words):
        ngram = nltk.wordpunct_tokenize(ngram_query)
        output = []
        for list in self.sentence:
            for i, word in enumerate(list):
                if word == ngram[0] and list[i+1] == ngram[1]:
                    Left = list[max(0,i - num_words): i]
                    Right = list[i + 2: (i + 2) + num_words]
                    Left_text = ' '.join(Left)[-self.left_context_length:].rjust(self.left_context_length)
                    Right_text = ' '.join(Right)[:self.right_context_length].ljust(self.right_context_length)
                    new_line = f"{Left_text} {ngram_query} {Right_text}"
                    output.append(new_line)
        if output:
            for line in output:
                print(line)
        else:
            print('"Query not found…"')
        
    def compute_bigram_stats(self, query, output_file_name):
        bigram = []
        for list in self.sentence:
            for i in range(len(list)):
                if list[i] == query and list[i+1].isalpha(): 
                    bigram.append(f"{list[i]} {list[i+1]}")
        bigram_count = Counter(bigram)        
        sorted = bigram_count.most_common()
        with open(output_file_name, 'w') as file:
            if sorted: 
                for bigram, num in sorted:
                    file.write(f"{bigram} {num}\n") 


cc = Concordancer()
cc.read_tokens('jane.txt')
cc.find_concordance("Chansbbwd", 7)
cc.find_concordance_ngram("sxwec lady", 7)
cc.compute_bigram_stats('ssssss', 'good_bigram.txt')