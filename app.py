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
        "Teclea posicición Pi (1 a 1,000,000):",
        min_value=1,
        max_value=len(pi_digits),
        value=1,
        step=1
    )

    # Perform the O(1) array lookup
    target_digit = pi_digits[position - 1]

    # Display the result in a clean metric visual box
    str.metric(label=f"Dígito en posición {position:,}", value=target_digit)


