import streamlit as str

# Set up the web page title
str.set_page_config(page_title="Pi Digit Finder", page_icon="🔢")
str.title("🔢 1 Million Digits of Pi Finder")
str.write("Enter a position to instantly retrieve the exact decimal digit of Pi.")

# Function to safely load the digits
@str.cache_data # This caches the file in RAM so it loads instantly for everyone
def load_pi():
    try:
        with open("pi.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

pi_digits = load_pi()

if not pi_digits:
    str.error("Error: 'pi.txt' data file not found in the directory.")
else:
    # Create a simple numeric input on the webpage
    position = str.number_input(
        "Enter Pi Position (1 to 1,000,000):",
        min_value=1,
        max_value=len(pi_digits),
        value=1,
        step=1
    )

    # Perform the O(1) array lookup
    target_digit = pi_digits[position - 1]

    # Display the result in a clean metric visual box
    str.metric(label=f"Digit at position {position:,}", value=target_digit)

