import math as m
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        line_free_spaces, line_words, remaining_words, line_last_space = self.helper(words, maxWidth)
        justified_text = []
        justified_line = self.create_line(line_free_spaces, line_words, remaining_words, line_last_space)
        justified_text.append(justified_line)
        while (remaining_words != []):
            line_free_spaces, line_words, remaining_words, line_last_space = self.helper(remaiing_words, maxWidth)
            justified_line = self.create_line(line_free_spaces, line_words, remaining_words, line_last_space)
            justified_text.append(justified_line)
        # print(justified_text)
        

    def helper(self, words, max_width):
        num_characters, last_space, line_words = 0, True, []
        remaining_words = words.copy()
        for word in words:
            word_num_characters = len(word)
            projected_num_characters = num_characters + word_num_characters
            num_space_available = max_width - projected_num_characters
            space_is_available = True if num_space_available > 0 else False
            just_enough = True if num_space_available == 0 else False
            if space_is_available: num_characters = projected_num_characters + 1 # the word's space
            elif just_enough:
                num_characters = projected_num_characters
                last_space = False
            else: break
            line_words.append(remaining_words.pop(remaining_words.index(word)))
        free_spaces = max_width - num_characters
        return (free_spaces, line_words, remaining_words, last_space)

    def create_line(self, free_spaces, line_words, remaining_words, need_last_word_space):
        word_index, word_count, line, word_space = 0, len(line_words), "", ' '
        free_space_slots = ubound_line_words = (word_count - 1)        
        word_spaces = word_count if need_last_word_space else free_space_slots
        free_spaces += word_spaces
        original_word_count = word_count
        print(free_spaces, word_count, line_words, remaining_words)
        if (remaining_words != []):
            while (free_spaces%2 != 0) and (word_count != 1):
                num_free_spaces_to_use = m.ceil(fress_spaces / free_space_slots)
                line += line_words[word_index] + (word_space * num_free_spaces_to_use)
                free_spaces -= num_free_spaces_to_use
                word_count -= 1
                word_index += 1
                free_space_slots -= 1
            while (word_index < ubound_line_words):
                num_free_spaces_to_use = free_spaces // free_space_slots
                line += line_words[word_index] + (word_space * num_free_space_to_use)
                free_spaces -= num_free_spaces_to_use
                word_index += 1
                free_space_slots -= 1
            if original_word_count == 1: line += line_words[word_index]+(word_space*free_spaces) 
            else: line += line_words[word_index]
            # else:
            #     while (word_index < ubound_line_words):
            #         line += line_words[word_index] + word_space
            #         free_spaces -= 1
            #         word_index += 1
            #     line += line_words[word_index] + (word_space * free_spaces)
        else:
            while (word_index < ubound_line_words):
                line += line_words[word_index] + word_space
                free_spaces -= 1
                word_index += 1
            line += line_words[word_index] + (word_space * free_spaces)
        return line


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16                        
my_sol = Solution()
my_sol.fullJustify(words, maxWidth)