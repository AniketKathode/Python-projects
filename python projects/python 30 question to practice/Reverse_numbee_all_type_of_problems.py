# Function to reverse a single word
def reverse_word(word):
    return word[::-1]

# Function to reverse a number (assuming positive integers)
def reverse_number(num):
    rev = 0
    num = int(num)  # Convert to integer
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

# Function to reverse the order of words in a sentence
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

# Function to reverse an array (list)
def reverse_array(arr):
    # Reverse the entire array
    return arr[::-1]

if __name__ == "__main__":
    n = input("Enter a sentence, word, number, or array (comma-separated): ")

    # Check if the input is a digit (number)
    if n.isdigit():
        result = reverse_number(n)

    # Check if it looks like an array (e.g., "1,2,3")
    elif "," in n:
        array = n.split(",")  # Split the string into a list
        array = [item.strip() for item in array]  # Remove any extra spaces
        result = reverse_array(array)

    # Check if it's a sentence (contains spaces)
    elif " " in n:
        result = reverse_sentence(n)

    # Otherwise, treat as a single word
    else:
        result = reverse_word(n)

    print("Reversed:", result)
