#test 2 

# Function to count occurrences of a pattern
def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

# Function to create a frequency map
def FrequencyMap(text, k):
    freq = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        freq[pattern] = freq.get(pattern, 0) + 1
    return freq

# Function to find frequent words
def FrequentWords(text, k):
    words = []
    freq = FrequencyMap(text, k)   #no need to write freqeuncy mape  code again
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words

# User interaction for selecting an operation
print("Select operation")
print("1. PatternCount")
print("2. FrequencyMap")
print("3. FrequentWords")

while True:
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        try:
            text = input("Enter the sequence: ")
            pattern = input("Enter the pattern: ")
            print("PatternCount:", PatternCount(text, pattern))
        except ValueError:
            print("Invalid input. Please enter valid text and pattern.")
            continue

    elif choice == '2':
        try:
            text = input("Enter the sequence: ")
            k = int(input("Enter the k-mer (integer): "))  # Ensure k is an integer
            print(FrequencyMap(text, k))
        except ValueError:
            print("Invalid input. Please enter valid text and an integer for k.")
            continue

    elif choice == '3':
        try:
            text = input("Enter the sequence: ")
            k = int(input("Enter the k-mer (integer): "))  # Ensure k is an integer
            print("Frequent Words:", FrequentWords(text, k))
        except ValueError:
            print("Invalid input. Please enter valid text and an integer for k.")
            continue

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    next_calculation = input("Let's do the next calculation? (yes/no): ")
    if next_calculation.lower() == "no":
        break
