def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Args:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.

    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    try:
        # Prompt the user to enter the original price and discount percentage
        original_price = float(input("Enter the original price: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the final price
        if final_price == original_price:
            print(f"No discount applied. The price remains: ${final_price:.2f}")
        else:
            print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the price and discount percentage.")

if __name__ == "__main__":
    main()
