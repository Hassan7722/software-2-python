from flask import Flask

app = Flask(__name__)
@app.route("/prime_number/<int:number>")
def check_prime(number):
    isPrime = True

    if number < 2:
        isPrime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False

    response = {
        "Number": number,
        "isPrime": isPrime
    }

    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3003)