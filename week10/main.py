from analyzer import TextAnalyser

def _parse_input() -> str:
    '''Parse input from the user.'''
    return input("Enter text to analyze: ")

def main():
    '''Main function to run the text analyzer.'''
    input_text = _parse_input()
    analyser = TextAnalyser(input_text)
    analysis_result = analyser.analyze()
    
    print("Analysis Result:")
    print(f"Total words: {analysis_result['total_words']}")
    print(f"Total uppercase words: {analysis_result['upper_words']}")

if __name__ == "__main__":
    main()
