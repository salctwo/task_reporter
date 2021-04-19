from flask import Response, request, redirect
from report_view import upload_view, profit_view, top_five_view, vendor_view
from report_service import report_total_profit, report_top_five_model, report_profit_per_vendor
from sale_model import Sale
import csv
import codecs

class Controller:
    def __init__(self, flask_app):
        
        @flask_app.route('/', methods = ['GET'])
        def index():
            return Response(upload_view(), mimetype = 'text/html')
        
        @flask_app.route('/', methods = ['POST'])
        def post():
            if 'myFile' not in request.files:
                return redirect(request.url)
            sales_file = request.files['myFile']
            salesreader = csv.reader(codecs.iterdecode(sales_file, 'utf-8'), delimiter=';', quotechar='|')
            sales = []
            next(salesreader)
            for row in salesreader:
                sales.append(Sale(row[0], row[1], int(row[2]), int(row[3])))
            filename = sales_file.filename 
            resp = profit_view(filename, report_total_profit(sales)) 
            resp += top_five_view(filename, report_top_five_model(sales))
            resp += vendor_view(filename, report_profit_per_vendor(sales))  
            
            return Response(resp, mimetype = 'text/html')


