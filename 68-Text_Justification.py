import math
# sentence = input("Please enter a sentence to get it back fully-justified!\n")
# words = sentence.split()
MAXWITDH = 25

class Solution:
    def justify_text(self, words: str, max_width: int) -> list[str]:
        free_spaces, line_words, remaining_words, last_space = self.helper(words, max_width)
        justified_text = []
        justified_line = self.create_line(free_spaces, line_words, remaining_words, last_space)
        justified_text.append(justified_line)
        while remaining_words != []:
            free_spaces, line_words, remaining_words, last_space = self.helper(remaining_words, max_width)
            justified_line = self.create_line(free_spaces, line_words, remaining_words, last_space)
            justified_text.append(justified_line)

        # OUTPUT
        print(justified_text)
        print(len(justified_text))

        for ln in justified_text:
            print(ln)
            print(len(ln))

    def helper(self, words, max_width):
        num_characters, line_words, last_space  = 0, [], True
        remaining_words = words.copy()
        for word in words:
            word_num_characters = len(word)
            print(word)
            projected_num_characters = num_characters +  word_num_characters
            print(projected_num_characters)
            num_space_available = max_width - projected_num_characters
            space_is_available = True if num_space_available > 0 else False
            just_enough = True if num_space_available == 0 else False
            print(space_is_available)
            if space_is_available: num_characters = projected_num_characters + 1 # for the word's space immediately after it
            elif just_enough: 
                num_characters = projected_num_characters
                last_space = False
            else: break    # Call it a day here!
            line_words.append(remaining_words.pop(remaining_words.index(word)))
            print(num_characters)
                
        free_spaces = max_width - num_characters
        return (free_spaces, line_words, remaining_words, last_space)

    def create_line(self, free_spaces, line_words, remaining_words, last_space = True):
        word_index = 0
        word_count = len(line_words)
        original_word_count = word_count
        ubound_line_words = free_space_slots = (word_count - 1)
        word_spaces = word_count if last_space else (word_count - 1)
        line, remaining_words_copy  = "", remaining_words.copy()
        print(free_spaces, word_count, line_words, remaining_words)       # played a very pivotal role in debuging
        free_spaces += word_spaces
        if remaining_words != []:
            while word_count != 1:
                line += line_words[word_index]+' '*(math.ceil(free_spaces/free_space_slots))
                free_spaces -= math.ceil(free_spaces/free_space_slots)
                free_space_slots -= 1
                word_index += 1
                word_count -= 1
            # while word_index < (ubound_line_words):
            #     line += line_words[word_index]+' '*(math.ceil(free_spaces/free_space_slots))
            #     free_spaces -= math.ceil(free_spaces/free_space_slots)
            #     free_space_slots -= 1
            #     word_index += 1
            #     word_count -= 1
            #     # if (free_space_slots%2 == 0):
            #     #     line += line_words[word_index]+' '*(free_spaces // free_space_slots)
            #     #     free_spaces -= (free_spaces // free_space_slots)
            #     #     free_space_slots -= 1
            #     #     word_index += 1
            #     # else:
                    
            if original_word_count == 1: line += line_words[word_index] + ' '*(free_spaces) 
            else: line += line_words[word_index]
        else:
            while word_index < (ubound_line_words):
                line += (line_words[word_index]+' ')
                word_index += 1
                free_spaces -= 1
            line += line_words[word_index]+' '*(free_spaces)
        return line

my_sol = Solution()
words = ["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."]
my_sol.justify_text(words, MAXWITDH)