# Experiment 5: File Handling and Modules
# TODO: Import count_words from the analyzer module

def main():
    try:
        # 1. Read input
        # TODO: Open 'input.txt' in read mode ('r')
        # TODO: Read the content into a variable named 'text'

        # 2. Process text
        # TODO: Call count_words(text) and store the result

        # 3. Write output
        # TODO: Open 'output.txt' in write mode ('w')
        # TODO: Write the result dictionary (convert to string first) to the file
        print("Result written to output.txt")

    except FileNotFoundError:
        print("Error: input.txt not found.")

if __name__ == "__main__":
    main()