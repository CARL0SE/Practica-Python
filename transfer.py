from distutils.log import debug
from urllib import response
from flask import Flask, request, render_template, make_response
app = Flask(__name__)

account_balance = 1000

@app.route('/', methods=['GET','POST'])
def transfer():
    global account_balance
    if request.method == 'POST':
        transfered_amount = request.form['amount']
        if transfered_amount.isdigit():
            account_balance -= int(transfered_amount)
    print(account_balance)
    response = make_response(render_template('transfer.html', balance=account_balance))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)