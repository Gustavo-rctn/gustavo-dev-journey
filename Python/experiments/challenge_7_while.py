def log_temperature(temp_list, new_temp):
    temp_list.append(new_temp)
    return temp_list

temperatures = []

while True:
    entry = input("Enter the temperature (or type 'exit' to quit): ").strip()
    if entry.lower() == 'exit':
        break

    temperatures = log_temperature(temperatures, float(entry))
    formatted_temps = ", ".join(f"{temp}°C" for temp in temperatures)
    print(f"Logged temperatures: {formatted_temps}\n")
