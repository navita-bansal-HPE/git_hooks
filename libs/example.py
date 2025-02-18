"""Module to add two numbers."""


def add_two_numbers(num1, num2):
    """Add two numbers and return their sum.

Args:
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    float: The addition of num1 and num2.
    """
    return num1 + num2

if __name__ == "__main__":
    # Prompt the user for input
    number1 = float(input("First number: "))
    number2 = float(input("\nSecond number: "))

    # Call the function to calculate the sum
    result = add_two_numbers(number1, number2)

    # Display the result
    print(f"The sum of {number1} and {number2} is {result}")
    print("T")
