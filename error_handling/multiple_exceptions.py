try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
except Exception as e:
    print(f"Error: {e}")