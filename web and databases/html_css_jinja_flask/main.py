from flask import Flask, render_template, request, url_for, redirect

# default folder is "templates" but if question specifies a name, it can be set using this parameter
app = Flask(__name__, template_folder="templates") 

@app.route('/')
def home():
    return render_template("tags.html")

# things of importance to note below:
# - no trailing slashes accomodate trailing slashes too
# - variable strings
# - different form methods to different files
# - accessing form requests
# - data sent to jinja
# - render template
@app.route('/secondary_page/<additional_string>', methods=["GET", "POST"])
def next_page(additional_string):
    if request.method == "GET":
        return render_template("css_cheat_sheet.html")
    elif request.method == "POST":
        text = request.form["input_text"]
        password = request.form["input_password"]
        random_numbers = [[1,2,3],[4,5,6],[5,6,7],[8,9,10],[11,12,13]]
        some_html_code = "<h3>Safe code</h3>"
        return render_template("using_jinja.html", text = text, password = password, the_list = random_numbers, some_html_code=some_html_code)

# variable urls
@app.route('/integer/<int:i>')
def integer_variable(i):
    return f"{i}"
@app.route('/float/<float:f>')
def float_variable(f):
    return f"{f}"
@app.route('/string/<s>')
def string_variable(s):
    return s

# redirecting to another function
@app.route('/stringredirect/<s>')
def stringredirect(s):
    return redirect(url_for('string_variable', s=s))

#redirecting to another url
@app.route('/redirectto')
def redirectto():
    return redirect("http://google.com")

# run
if __name__ == "__main__":
    app.run(debug=True)