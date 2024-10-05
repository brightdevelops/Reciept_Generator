from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the form input page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the receipt generation
@app.route('/receipt', methods=['POST'])
def receipt():
    items = []
    num_items = int(request.form['num_items'])

    for i in range(1, num_items + 1):
        item_name = request.form[f'item_name_{i}']
        quantity = int(request.form[f'quantity_{i}'])
        price = float(request.form[f'price_{i}'])
        items.append((item_name, quantity, price))

    subtotal = sum(quantity * price for _, quantity, price in items)
    tax = subtotal * 0.10  # 10% tax
    total = subtotal + tax

    return render_template('receipt.html', items=items, subtotal=subtotal, tax=tax, total=total)

if __name__ == "__main__":
    app.run(debug=True)
