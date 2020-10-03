from flask import Flask, render_template, request, redirect
from company_dict import return_company_dictionary
import create_fond

app = Flask(__name__)


def create_tupellist_from_dict(data):
    tupellist = []
    for i in range(round(len(data)*0.5)):
        entity1 = "asset" + str(i)
        entity2 = "percentage" + str(i)
        tupellist.append((data[entity1], data[entity2]))
    companies = return_company_dictionary()
    symbol_list = []
    for tupel in tupellist:
        company = tupel[0]
        percentage = tupel[1]
        if company in companies:
            symbol_list.append((companies[company], percentage))
    return symbol_list




@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit_selection', methods=['POST', 'GET'])
def submit_selection():
    if request.method == 'POST':
        data = request.form.to_dict()
        tupellist = create_tupellist_from_dict(data)
        # fond_data_points = create_fond.build_fond(tupellist)
        print(tupellist)
        return 'ok'

    else:
        return 'wrong'


if __name__ == '__main__':
    app.run()
