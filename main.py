from flask import Flask
import os
from report_controller import Controller

app = Flask(__name__)
controller = Controller(app)

port = os.getenv('PORT', 8081)

app.run(host='0.0.0.0', port=port)

