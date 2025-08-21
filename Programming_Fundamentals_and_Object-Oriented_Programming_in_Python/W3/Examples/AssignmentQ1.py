def get_index(word, words):
    i = 0
    for w in words:
        if word == w:
            return i
        i = i + 1
    return -1

def get_max_indx(count):
    maximum = -1
    max_indx = -1
    for i in range(len(count)):
        if maximum < count[i]:
            maximum = count[i]
            max_indx = i
    return max_indx

words = []
count = []

filename = input("Enter filename: ")
with open(filename, "r") as f:
    content = f.read()
    all_words = content.lower().split()
    print(f"Number of words in the file is: {len(all_words)}")
    for word in all_words:
        indx = get_index(word, words)
        if indx == -1:
            words.append(word)
            count.append(0)
        else:
            count[indx] = count[indx] + 1
    print(f"The word most appeared is: {words[get_max_indx(count)]}")
    f.close()
