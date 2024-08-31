import string

def count_words_in_paragraph(file_path):
   
    word_count = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = line.split()
                
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        
        # Sort the dictionary by word (alphabetical order)
        sorted_word_count = dict(sorted(word_count.items()))

        return sorted_word_count

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


file_path = "paragraph.txt"
word_count = count_words_in_paragraph(file_path)
    
if word_count:
     
     print("Word Count (in alphabetical order):")
     for word, count in word_count.items():
            
            print(f"{word}: {count}")
