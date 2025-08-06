from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return "<h1>Welcome to WizCracker Secure Notes</h1>"

@app.route('/notes')
def list_notes():
    return "<br>".join(notes)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        content = request.form['content']
        notes.append(content)
        return redirect(url_for('list_notes'))
    return '''
        <form method="post">
            <textarea name="content"></textarea>
            <input type="submit" value="Save">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

API_SECRET = "hardcoded-super-secret-key"
