
# import os
from flask import Flask, flash, redirect, render_template, request, url_for

subu = Flask(__name__)
# subu.config['SECRET_KEY'] = 'subuliti'
# port = int(os.environ.get('PORT', 3000))


@subu.route('/')
def home():
    return render_template("home.html")


@subu.route('/addJoiner', methods=['GET', 'POST'])
def addJoiner():
    zwj = "\u200d"
    emo_add = []

    for key in request.form.items():
        emo_add = key[1]

    string = ''
    for i in range(len(emo_add)):
        string += zwj + emo_add[i]

    return render_template('home.html', add='New Emoji: {}'.format(string))


@subu.route('/removeJoiner', methods=['GET', 'POST'])
def removeJoiner():
    zwj = "\u200d"
    temp = sep = ''
    #sep =''
    j = 0

    for key in request.form.items():
        emo = key[1]
    for i in range(len(emo)):
        if emo[i] != zwj:
            if j == 0:
                temp = emo[i]
            else:
                temp += sep + emo[i]
            j += 1

    return render_template('home.html', remove='Emoji is built of: {}'.format(temp))


if __name__ == '__main__':
    subu.run(debug=True)
    # subu.run(host='0.0.0.0', port=port)
