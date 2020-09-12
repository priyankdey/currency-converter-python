# Python program to convert the currency 
# of one country to that of another country 

# Import the modules needed 
import requests 

class Currency_convertor: 
    # empty dict to store the conversion rates 
    rates = {} 
    def __init__(self, url): 
        data = requests.get(url).json() 

        # Extracting only the rates from the json data 
        self.rates = data["rates"] 

    # function to do a simple cross multiplication between 
    # the amount and the conversion rates 
    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'EUR' : 
            amount = amount / self.rates[from_currency] 

        # limiting the precision to 2 decimal places 
        amount = round(amount * self.rates[to_currency], 2) 
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency)) 

# Driver code 
if __name__ == "__main__": 

    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io' 
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', 'd6ada21caa50a28c89c3014e3c8a7d80') 
    c = Currency_convertor(url) 
    from_currency = input("From Currency: ").upper() 
    to_currency = input("To Currency: ").upper() 
    amount = int(input("Amount: ")) 

    c.convert(from_currency, to_currency, amount) 
