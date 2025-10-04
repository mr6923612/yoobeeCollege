'''activaty_1.py
analyser
analyzing the text inputs.
'''

class TextAnlyser:
    '''A class to analyze imput_text.'''
    def __init__(self, imput_text):
        self.text = imput_text

    # calculate the total number of words.
    def count_words(self)->int:
        '''Count the total number of words in the text.'''
        words = self.text.split()
        return len(words)

    # determine the upper words count.
    def count_upper_words(self)->int:
        '''Count the number of uppercase words in the text.'''

        words = self.text.split()
        upper_words = [word for word in words if word.isupper()]
        return len(upper_words)

if __name__ == "__main__":
    #text = "Hello World. THIS is a TEST. Python is GREAT."
    text = input("Enter the text to be analyzed: ")
    analyser = TextAnlyser(text)
    print("Total words:", analyser.count_words())
    print("Total uppercase words:", analyser.count_upper_words())
