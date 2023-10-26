
print("US Dollar to Euro in Python")

dollar = float(input("enter dollar value : "))
euro = dollar * 0.94540
print("$" + str(dollar) + " " + "dollar is equivalent to " + str(euro) + " " + "European Euros") 
YN = input("Do you want to convert a number again?: y/n")
while YN == "y":
    dollar = float(input('enter dollar value : '))
    euro = dollar * 0.94540
    print("$" + str(dollar) + " " + "dollar is equivalent to " + str(euro) + " " + "European Euros")
    YN = input("Do you want to convert a number again?: y/n")