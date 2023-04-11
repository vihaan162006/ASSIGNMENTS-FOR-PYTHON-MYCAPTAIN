 def most_frequent(string):
 freq_dict = {}
 for char in string:
 if char != ' ':
 freq_dict[char] = freq_dict.get(char, 0) + 1
 sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
 for item in sorted_freq:
 print(f"{item[0]} = {item[1]:02d}")
        
most_frequent("Please enter a string Mississippi")
