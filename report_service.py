from sale_model import Sale

def report_total_profit(sales):
    """
    Implement me:
        `sales` parameter is a list of 'Sale' object (more info see `sale_model.py`).
        If a given variable 's' is of type 'Sale' you can say access to its properties like: s.vendor, s.model, s.price or s.quantity.
        This function should return a numberic value for the tatal profit for the sales.
        Bare in mind that one item has 'price' and 'quantity', meaing that if the item's price is 100 but there were 5 unit sold (quantity)
        We need to say (100 x 5) = 500.
        See first test case in `test.py` file for an example of how the return type should look like."""

    total_profit = 0
    for sale in sales:
        total_profit += sale.price * sale.quantity

    return total_profit

def report_top_five_model(sales):
    """
        Implement me:
            `sales` parameter is a list of 'Sale' object (more info see `sale_model.py`).
            If a given variable 's' is of type 'Sale' you can say access to its properties like: s.vendor, s.model, s.price or s.quantity.
            This function should return a list of strings, sorted desc, meaning if "Pixel XL" is the most sold model it should be first.
            e.g. ["Pixel XL", "Moto E", "Xiaomi M1", "Sony XL", "Blackberry LTD"] where Moto E is the second most sold and Xiaomi M1 the third.
            See second test case in `test.py` file for an example of how the return data should look like."""
    list_sales = []
    model_and_price = ()
    top_models = []
    
    for sale in sales:
        model_and_price = ((sale.price * sale.quantity), sale.model)
        list_sales.append(model_and_price)

    copy_list = sorted(list_sales, reverse=True)
    for model in copy_list:
        top_models.append(model[1])

    return top_models[:5]
     
def report_profit_per_vendor(sales):
    """
    Implement me:
        `sales` parameter is a list of 'Sale' object (more info see `sale_model.py`).
        If a given variable 's' is of type 'Sale' you can say access to its properties like: s.vendor, s.model, s.price or s.quantity.
        This function should return a dictionary with name of vendor as key and value as the profit.
        See third test case in `test.py` file for an example of how the return data should look like. 
        """

    vendors_and_profit = {}
    for sale in sales:
        if sale.vendor in vendors_and_profit:
            vendors_and_profit[sale.vendor] += sale.price * sale.quantity
        else:
            vendors_and_profit[sale.vendor] = sale.price * sale.quantity

    return vendors_and_profit

