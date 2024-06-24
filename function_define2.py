def addition(a,b):
    return a + b

# Main program
def main():
    input_a = float(input("What is the first number?\n"))
    input_b = float(input("What is the second number?\n"))

    # Returning a result
    result = addition(input_a, input_b)
    print("The sum of these numbers is", (str(result)))

main()