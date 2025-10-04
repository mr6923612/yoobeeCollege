''' analyzer.py
provide a object-oriented approach to analyze text inputs.
'''
class TextAnalyser:
    '''A class to analyze input_text.'''
    def __init__(self, input_text):
        if not isinstance(input_text, str):
            raise ValueError("Input must be a string.")
            
        self.text = input_text


    # calculate the total number of words.
    def count_words(self) -> int:
        '''Count the total number of words in the text.'''
        return len(self.text)

    # determine the upper words count.
    def count_upper_words(self) -> int:
        '''Count the number of uppercase words in the text.'''
        total=0
        for i in self.text:
            if i.isupper():
                total+=1

        return total
    
    def analyze(self):
        '''Perform a comprehensive analysis of the text.'''
        total_words = self.count_words()
        upper_words = self.count_upper_words()
        return {
            "total_words": total_words,
            "upper_words": upper_words
        }
