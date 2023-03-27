from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        name = request.form.get('name')
        month = request.form.get("month")
        day = request.form.get("day")

        # Validation for empty name and negative month and day.
        if not name or int(month) < 1 or int(day) < 1:
            return render_template("failure.html")
        
        # Add to the database
        database.add_entry(name, month, day)
        return redirect('/')

    else:
        birthdays = database.get_all_birthdays()
        return render_template('index.html', birthdays=birthdays)
    

# Endpoint for deleting a record
@app.route("/delete/<id>", methods = ['GET', 'POST'])
def delete(id):
    database.remove_birthday(id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
    