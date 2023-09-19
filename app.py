from flask import Flask,render_template
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = Flask(__name__)
engine = create_engine('postgresql://postgres:123@1.2.3.4:5432/new_lk')

def gerquerytext():
    return ''

@app.route('/')
def index() -> str:
    return render_template("Home.html")

@app.route("/Requests")
def get_page_requests():
    with engine.connect() as connection:
        result = connection.execute(text("select * from v1_request_list_get('f5d4baa2-69ef-fbba-11ec-c252aa391579','6b3258b4-5e51-43e5-aaf0-9cd9f0fec8c8')"))
        return render_template("Pages/Requests.html", h1 ="Обращения", data = result.fetchall())

@app.route("/Finance")
def get_page_Finance():
    return render_template("Pages/Finance.html", h1 ="Финансы")

@app.route("/Documents")
def get_page_Documents():
    return render_template("Pages/Documents.html", h1 ="Документы")

@app.route("/Сounters")
def get_page_Сounters():
    return render_template("Pages/Сounters.html", h1 ="Счетчики")

@app.route("/News")
def get_page_News():
    return render_template("Pages/News.html", h1 ="Новости")

@app.route("/Contacts")
def get_page_Contacts():
    return render_template("Pages/Contacts.html", h1 ="Контакты")

@app.route("/Home")
def get_page_Home():
    return render_template("Home.html", h1 ="Личный кабинет SMINEX")

@app.route("/Request/<request_id>")
def get_page_Request(request_id):
    with engine.connect() as connection:
        result = connection.execute(text(f"select * from v1_getrequestbyid({request_id})"))
        return render_template("Pages/Request.html", h1 ="Обращение", data=result.fetchall())

@app.route("/Payment")
def get_page_Payment():
    return render_template("Pages/Payment.html", h1 ="Оплата задолженности")

if __name__ == '__main__':
    app.run(debug=False)