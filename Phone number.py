print("Method 1:")
def phone_number(country_code, area_code, first_3_digits, last_4_digits):
    print(f"+{country_code}-{area_code}-{first_3_digits}-{last_4_digits}")

phone_number(91, 670, 234, 4567)

print("--------------------------")

print("Method 2:")
def phone_number(country_code, area_code, first_3_digits, last_4_digits):
    return f"{country_code}-{area_code}-{first_3_digits}-{last_4_digits}"

number = phone_number(country_code=91 , area_code=123, first_3_digits=456, last_4_digits=7890)

print(number)






