#Resources used not mentioned in assignment:
#https://www.programiz.com/python-programming/time
#https://docs.python.org/3/library/time.html

import time

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None

def speed_typing_test():
    #Prompt the user for the path to the text file
    file_path = input("Enter the path to your text file: ")

    #Read the text from the specified file
    text_to_type = read_text_from_file(file_path)

    if text_to_type is None:
        return

    #Display the text to the user
    print("Type the following text as fast as you can:")
    print(text_to_type)

    #Wait for the user to press Enter before starting the typing test
    input("Press Enter when you are ready to start typing...")

    #Record the start time
    start_time = time.time()

    #Prompt the user to type the text
    user_input = input("Start typing: ")

    #Record the end time
    end_time = time.time()

    #Calculates the time taken
    elapsed_time = end_time - start_time

    #Check if the typed text matches the original text
    if user_input.strip() == text_to_type.strip():
        print(f"Congratulations! You typed it correctly in {elapsed_time:.2f} seconds.")
        words_per_minute = len(text_to_type.split()) / (elapsed_time / 60)
        print(f"Your speed is approximately {words_per_minute:.2f} words per minute.")
    else:
        print("It seems like there was a mistake in your typing. Try again.")

if __name__ == "__main__":
    #Call the main function to run the speed typing test
    speed_typing_test()
