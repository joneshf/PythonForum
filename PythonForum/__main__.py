from . import app

if __name__ == '__main__':
    # Deploy the development app.
    # This is only accessible when tunneled into the machine via the guest ssh account.
    app.run(host="127.0.0.1", port=8080)