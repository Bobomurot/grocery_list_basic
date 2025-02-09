import csv

# Define function to retrieve prices colum in to a list
def get_prices(data):
    """
    Retrieves prices column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of prices
    """
    prices = []
    r = 0
    for line in data:
        if r != 0:
            prices.append(float(line[2][1: :]))
            
        r += 1
    #prices.pop(0)
    return prices
       
    



def get_products(data):
    """
    Retrieves products column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of products
    """
    products = []
    prr = 0
    for pro in data:
        if prr != 0:
            products.append(pro[0])
        
        prr += 1
    return products
    

def get_expensive(prices):
    """
    Finds the most expensive product of index

    Args:
        prices (list): list of prices

    Returns:
        int: index of most expensive product
    """
    max_index = prices.index(max(prices))
    return max_index
    

# Read data from file
f = open("data.csv", "r")
reader_data = csv.reader(f) 
a = get_prices(reader_data)
#p = get_products(reader_data)
#print(a)
#print(p)
e = get_expensive(a)
print(e)
    

