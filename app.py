
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
notes = []

template = '''
<!doctype html>
<title>Wizcracker Notes</title>
<h1>Take a Note</h1>
<form method=post>
  <input type=text name=title placeholder="Title" required>
  <br><br>
  <textarea name=content placeholder="Note content" rows=4 cols=50 required></textarea>
  <br><br>
  <input type=submit value=Save>
</form>
<hr>
<h2>Saved Notes</h2>
<ul>
{% for note in notes %}
  <li><strong>{{ note.title }}</strong>: {{ note.content }}</li>
{% else %}
  <li>No notes yet.</li>
{% endfor %}
</ul>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        notes.append({
            "title": request.form["title"],
            "content": request.form["content"]
        })
        return redirect("/")
    return render_template_string(template, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
