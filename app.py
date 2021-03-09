from flask import Flask, render_template, request, redirect
from lib.manager import Manager, FileManager
from lib.forms import SellForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dda122182f7cef59f3663789ab631351"
manager = Manager()
file_manager = FileManager()


@manager.assign("saldo", 2)
def balance_update(manager, amount, comment):
    if manager.balance + int(amount) >= 0:
        manager.balance += int(amount)


@manager.assign("zakup", 3)
def buy(manager, product_name, price, amount):
    if manager.balance - int(price)*int(amount) >= 0:
        manager.balance -= int(price)*int(amount)
        if product_name not in manager.stock:
            manager.stock[product_name] = int(amount)
        else:
            manager.stock[product_name] += int(amount)
    else:
        print("Brak wystarczającej ilość gotówki.")


@manager.assign("sprzedaz", 3)
def sell(manager, product_name, price, amount):
    if product_name not in manager.stock:
        print("Brak produktu w magazynie!")
    elif manager.stock[product_name] >= int(amount):
        manager.stock[product_name] -= int(amount)
        manager.balance += int(price)*int(amount)
    else:
        print("Brak wystarczającej ilości")


""" @app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(dict(request.form))
        file_manager.data.append("saldo")
        for change in request.form.items():
            file_manager.data.append(change[1])
        file_manager.save_data()
        manager.stock = {}
        manager.balance = 0
        file_manager.data = []
        file_manager.open_file()
        file_manager.file_process(manager)
        return redirect("/")
    return render_template("index.html", manager=manager)


@app.route("/saldo", methods=['GET', 'POST'])
def saldo():
    if request.method == 'POST':
        print(dict(request.form))
        file_manager.data.append("saldo")
        for change in request.form.items():
            file_manager.data.append(change[1])
        file_manager.save_data()
        manager.stock = {}
        manager.balance = 0
        file_manager.data = []
        file_manager.open_file()
        file_manager.file_process(manager)
        return redirect("/saldo")
    return render_template("index.html", manager=manager)


@app.route("/zakup", methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        print(dict(request.form))
        file_manager.data.append("zakup")
        for change in request.form.items():
            file_manager.data.append(change[1])
        file_manager.save_data()
        manager.stock = {}
        manager.balance = 0
        file_manager.data = []
        file_manager.open_file()
        file_manager.file_process(manager)
        return redirect("/zakup")
    return render_template("zakup.html", manager=manager) """


@app.route("/", methods=['GET', 'POST'])
def saldo():
    if request.method == 'POST':
        print(dict(request.form))
        for change in request.form.items():
            file_manager.data.append(change[1])
        file_manager.save_data()
        manager.stock = {}
        manager.balance = 0
        file_manager.data = []
        file_manager.open_file()
        file_manager.file_process(manager)
        return redirect("/")
    return render_template("index.html", manager=manager)


@app.route("/sprzedaz", methods=['GET', 'POST'])
def sell():
    form = SellForm()
    return render_template("sprzedaz.html", form=form, manager=manager)


file_manager.open_file()
file_manager.file_process(manager)
