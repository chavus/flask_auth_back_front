from auth_api import app
from flask import redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('core.home'))

# application = app

if __name__ == "__main__":
    app.run(port=5000, debug=True)
