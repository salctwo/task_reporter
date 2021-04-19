def upload_view():
    return """
    <p>Click on the "Choose File" button to upload csv sales file: </p>
    <form action="/" method="post" enctype=multipart/form-data >
    <input type="file" id="myFile" name="myFile">
    <input type="submit" value="Do report">
    </form>
    """

def profit_view(filename, total_profit):
    total = "£{:,.2f}".format(total_profit)
    return f"""<h1> Report: {filename} </h1>
    <hr/><h2>Total profit: {total}</h2>
    """

def top_five_view(filename, models):
    html = "<hr/><h2>Top 5 most sold models: </h2>"
    for i in range(len(models)):
        html += f"<h{i+2}>{models[i]}</h{i+2}>"
    return html

def vendor_view(filename, vendors):
    html = "<hr/><h2>Profit per vendors: </h2>"
    for key in vendors:
        (v,p) = (key, vendors[key])
        total = "£{:,.2f}".format(p)
        html += f'<p><b>Vendor<b/>: {v}, <b>Profit</b>: {total}</p>'
    return html

    
