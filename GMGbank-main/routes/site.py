from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

site_route = Blueprint('site_route', __name__)

# Lista global para armazenar todos os comprovantes de transferência
all_transfers = []


@site_route.route('/')
def home():
    return render_template('index.html')


@site_route.route('/transfer/<int:id>', methods=['GET', 'POST'])
def transfer(id):
    message = request.args.get('message')
    success = request.args.get('success', 'False') == 'True'
    if request.method == 'POST':
        account_number = request.form['account_number']
        recipient_name = request.form['recipient_name']
        transfer_amount = request.form['transfer_amount']
        transfer_description = request.form.get('transfer_description', '')

        if process_transfer(id, account_number, recipient_name, transfer_amount, transfer_description):
            global all_transfers
            new_transfer = {
                'id': len(all_transfers) + 1,
                'account_number': account_number,
                'recipient_name': recipient_name,
                'transfer_amount': transfer_amount,
                'transfer_description': transfer_description,
                'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
            all_transfers.append(new_transfer)
            return redirect(
                url_for('site_route.transfer', id=id, message='Transferência realizada com sucesso', success='True'))
        else:
            return redirect(url_for('site_route.transfer', id=id,
                                    message='Erro ao realizar a transferência. Verifique os dados e tente novamente.'))

    return render_template('tranfer.html', id=id, message=message, success=success)


@site_route.route('/receipts/<int:id>')
def receipts(id):
    transfer = next((t for t in all_transfers if t['id'] == id), None)
    return render_template('receipts.html', transfer=transfer)


@site_route.route('/all_receipts')
def all_receipts():
    return render_template('all_receipts.html', transfers=all_transfers)


@site_route.route('/account/<int:id>')
def account(id):
    return render_template('account.html', id=id)


def process_transfer(user_id, account_number, recipient_name, transfer_amount, transfer_description):
    return True
