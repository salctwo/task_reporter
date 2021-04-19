def report_total_profit(sales):
    result = 0
    for s in sales:
        result = result + (s.price * s.quantity)
    return result

def report_top_five_model(sales):
    report = {}
    for s in sales:
        if s.model in report:
            t = report[s.model]
            report[s.model] = t + (s.price * s.quantity)
        else:
            report[s.model] = s.price * s.quantity
    ls = [(k,v) for k,v in report.items()]
    ls.sort(reverse=True, key= lambda a: a[1])
    ls = list(map(lambda a: a[0], ls))
    return ls[:5]

def report_profit_per_vendor(sales):
    vendors = {}
    for s in sales:
        if s.vendor in vendors:
            t = vendors[s.vendor]
            vendors[s.vendor] = t + (s.price * s.quantity)
        else:
            vendors[s.vendor] = s.price * s.quantity
    return vendors 

