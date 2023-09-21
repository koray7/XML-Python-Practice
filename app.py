from flask import Flask, render_template, request, redirect, url_for, flash, session

from flask_session import Session
import xml.dom.minidom


app = Flask(__name__)
app.secret_key = 'Austin7'

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
app.config['INCORRECT_ATTEMPTS'] = 0


def get_person_info(person_id):
    domtree = xml.dom.minidom.parse('people.xml')
    group = domtree.documentElement
    people = group.getElementsByTagName('person')

    for person in people:
        if person.getAttribute('id') == person_id:
            name = person.getElementsByTagName(
                'name')[0].childNodes[0].nodeValue
            age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
            weight = person.getElementsByTagName(
                'weight')[0].childNodes[0].nodeValue
            height = person.getElementsByTagName(
                'height')[0].childNodes[0].nodeValue

            return {
                'Name': name,
                'Age': age,
                'Weight': weight,
                'Height': height
            }

    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET', 'POST'])
def show_person_info():
    if request.method == 'POST':
        person_id = request.form.get('person_id')
        person_info = get_person_info(person_id)

        if person_info:
            app.config['INCORRECT_ATTEMPTS'] = 0
            session['search_results'] = person_info
            return render_template('person_info.html', person_info=person_info)
        else:
            app.config['INCORRECT_ATTEMPTS'] += 1
            if app.config['INCORRECT_ATTEMPTS'] > 1:
                flash_message = "You entered an invalid ID number. Please try another."
                flash(flash_message)

    return render_template('person_form.html')


@app.route('/search', methods=['GET', 'POST'], endpoint='search_person')
def search_person():
    flash_message = session.pop('flash_message', None)

    # Check if search_results is already set in the session
    search_results = session.get('search_results', None)

    return render_template('person_form.html', flash_message=flash_message, search_results=search_results)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=3000)
