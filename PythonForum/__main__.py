from . import app

if __name__ == '__main__':
    # Run the app in a development environment.
    # For deployment do not execute __main__.py
    app.run(host="0.0.0.0", port=8080)