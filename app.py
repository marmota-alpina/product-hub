from config import db, app
from routes import api_view, config_api_view

app.register_api_view(api_view)
app.register_api_view(config_api_view)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
