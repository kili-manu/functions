
#Question one
def area_of_circle(r, pi):
    area = pi * r ** 2
    return round(area, 2)

area_input=input("Enter the radius of the circle: ")
area=area_of_circle(int(area_input), 3.14159)
print(area)

#End of #Question one


#Question two

def find_net_income(money, tax):

    due=money+( money* tax/100)
    return round(due, 2)

print("\nProvide the amount of money and tax rate")
amount_input=input("Enter the amount of money: ")
tax_input=input("Enter the tax rate: ")
due= find_net_income(int(amount_input), int(tax_input))

print(due)


#End of #Question two


#Question three

def convert_fahrenheit_to_celcius(fahrenheit):
    celcius=(fahrenheit - 32 )* 5/9
    return round(celcius, 4)
fahrenheit_value=input("\nEnter the value of the fahrenheit: ")
celcius=convert_fahrenheit_to_celcius(int(fahrenheit_value))
print(celcius)

#End of #Question three





