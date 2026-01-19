from flask import Flask, render_template, request

app = Flask(__name__)

# List to store notes in memory
notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        # Only add the note if the input is not empty
        if note:
            notes.append(note)
            
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)