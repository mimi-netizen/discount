def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount, with a minimum discount 
  of 20%.

  Args:
      price: The original price of the item.
      discount_percent: The discount percentage (0-100).

  Returns:
      The final price after applying the discount (minimum 20% discount).
  """
  if discount_percent >= 20:
    discount = price * discount_percent / 100
    final_price = price - discount
  else:
    final_price = price
  return final_price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (0-100): "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount_percent)
print(f"Final price after discount: ${final_price:.2f}")
