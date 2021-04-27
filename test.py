from report_service import *
from sale_model import Sale

def test(title, result, expected):
    try:
        assert expected == result
        print(title + ' ✅')
    except AssertionError:
        print(title + f', expected: {expected}, but result: {result} ❌')

sales = [
    Sale('Moto E (1st generation)', 'Motorola Mobility', 460, 2),
    Sale('OnePlus 8', 'OnePlus', 260, 2),
    Sale('Pixel 2/XL', 'Google', 430, 4),
    Sale('Pixel 2/XL', 'Google', 430, 5),
    Sale('Xiaomi Mi 9/SE', 'Xiaomi', 276, 3),
    Sale('Samsung Galaxy Note Edge', 'Samsung Electronics', 272, 4),
    Sale('Moto E3', 'Motorola Mobility', 287, 2),
    Sale('OnePlus 9 Pro', 'OnePlus', 426, 1),
    Sale('LG K31', 'LG Electronics', 421, 1)
]


test('Total profits for above sales should be', report_total_profit(sales), 8647)

test('Top 5 most sold models should be', report_top_five_model(sales), 
        ['Pixel 2/XL', 'Samsung Galaxy Note Edge', 'Moto E (1st generation)', 'Xiaomi Mi 9/SE', 'Moto E3'])

test('Profit per vendor should be', report_profit_per_vendor(sales), 
        {'Motorola Mobility': 1494, 'OnePlus': 946, 'Google': 3870, 'Xiaomi': 828, 'Samsung Electronics': 1088, 'LG Electronics': 421} )
