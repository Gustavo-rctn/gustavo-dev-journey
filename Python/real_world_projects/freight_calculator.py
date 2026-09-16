# System Inputs
package_weight_kg = float(input('Enter package weight (kg): '))
distance_km = float(input('Enter delivery distance (km): '))

# Base Calculation (R$ 2.50 per km)
shipping_cost = distance_km * 2.50

# Weight Surcharge Rule
if package_weight_kg > 10:
    shipping_cost += 20.00  # Equivalent to: shipping_cost = shipping_cost + 20.00
    print('Heavy package fee applied (+ $20.00).')

# Long Distance Discount Rule
if distance_km > 100:
    discount = shipping_cost * 0.10
    shipping_cost -= discount  # Equivalent to: shipping_cost = shipping_cost - discount
    print(f'Long distance discount applied (- $ {discount:.2f}).')

# Final Transaction Summary
print('\n--- SHIPPING SUMMARY ---')
print(f'Package Weight: {package_weight_kg:.1f} kg')
print(f'Delivery Distance: {distance_km:.1f} km')
print(f'Final Shipping Fee: $ {shipping_cost:.2f}')