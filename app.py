from flask import Flask, render_template, request, redirect
from company_dict import return_company_dictionary
import create_fond
import pprint

app = Flask(__name__)


def create_tupellist_from_dict(data):
    tupellist = []
    for i in range(round(len(data) * 0.5)):
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


def y_numbers(normalized_data):
    y_list = []
    for tupel in normalized_data:
        y_list.append(tupel[1])
    y_list.reverse()
    return y_list


def x_numbers(normalized_data):
    x_data = []
    for i in normalized_data:
        x_data.append(i[0])
    for i in range(len(x_data)):
        if i % 10 != 0:
            x_data[i] = ""
    x_data.reverse()
    return x_data


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit_selection', methods=['POST', 'GET'])
def submit_selection():
    if request.method == 'POST':
        data = request.form.to_dict()
        tupellist = create_tupellist_from_dict(data)
        fond_data_points = create_fond.build_fond(tupellist)
        normalized_data = create_fond.norm_fond(fond_data_points, tupellist)
        print(normalized_data)
        x_data = x_numbers(normalized_data)
        y_data = y_numbers(normalized_data)
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(normalized_data)
        # print(tupellist)
        # y_data = [0, 10, 5, 2, 20, 30, 45]
        # x_data = ["January", "February", "March", "April", "May", "June", "July"]
        print(y_data)
        return render_template('show_fond.html', x_data=x_data, y_data=y_data)

    else:
        return 'wrong'


if __name__ == '__main__':
    app.run()
