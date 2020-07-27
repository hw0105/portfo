from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
# print(__name__)


def write_to_file(data):
    with open("./database.txt", mode="a") as my_file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = my_file.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open("database.csv", newline='\n', mode='a') as database:
        csv_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])


@app.route("/")
def my_home():
    # print(url_for('static', filename='pikachu.ico')) A safe way to store the url
    # returns the html file to display
    return render_template("index.html")


@app.route('/<string:linkname>')
def about(linkname):
    return render_template(linkname)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            write_to_file(data)
            return redirect("/thankyou.html")
        except:
            return "Please try again..."
    else:
        return "Something went wrong. Try again!"
    # @app.route('/works.html')
    # def next_page():
    #     return render_template("works.html")

    # @app.route("/about.html")
    # def about_me():
    #     return render_template("about.html")

    # @app.route("/contact.html")
    # def contact():
    #     return render_template("contact.html")

    # @app.route("/components.html")
    # def comp():
    #     return render_template("components.html")
