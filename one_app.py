from flask import *
from static import *
from templates import *


app = Flask(__name__)

@app.route("/")
def index():

    return render_template(index.html)




if __name__ == "__main__":
    app.run(debug=True)

    
