from flask import Blueprint, render_template

site_route = Blueprint('site', __name__)

@site_route.route('/')
def home():
    return render_template('index.html')

@site_route.route('/transfer<int:id>')
def transfer(id):
    return render_template('transfer.html', id=id)

@site_route.route('/receipts<int:id>')
def receipts(id):
    return render_template('receipts.html', id=id)   

@site_route.route('/account<int:id>')
def account(id):
    return render_template('account.html', id=id)
