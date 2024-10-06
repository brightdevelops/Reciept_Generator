from flask import Flask, render_template, request

app = Flask(__name__)

# Function to generate receipt details
def generate_receipt(items):
    subtotal = 0
    receipt = []
    
    for item, quantity, price in items:
        total_price = quantity * price
        subtotal += total_price
        receipt.append({'item': item, 'quantity': quantity, 'price': price, 'total_price': total_price})
    
    tax = subtotal * 0.10  # 10% tax
    total = subtotal + tax

    return receipt, subtotal, tax, total

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and generate receipt
@app.route('/receipt', methods=['POST'])
def receipt():
    items = []
    num_items = int(request.form['num_items'])

    for i in range(num_items):
        item_name = request.form[f'item_name_{i+1}']
        quantity = int(request.form[f'quantity_{i+1}'])
        price = float(request.form[f'price_{i+1}'])
        items.append((item_name, quantity, price))

    receipt, subtotal, tax, total = generate_receipt(items)
    return render_template('receipt.html', receipt=receipt, subtotal=subtotal, tax=tax, total=total)

if __name__ == '__main__':
    app.run(debug=True)