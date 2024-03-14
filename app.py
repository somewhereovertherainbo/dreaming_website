import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

dreams = [{
    'title':
    'Heights',
    'landscape':
    'Muddy roads',
    'Time of day':
    'Night time',
    'description':
    'I am situated on a very high construction equipment, it is night time and I can see some lights of the city. I look down and it is a very wide muddy road with railway tracks drowned in mud. High speed Indian trains are just sliding on those muddy tracks.'
}, {
    'title':
    'Vast lands',
    'landscape':
    'Hard vast deserty lands',
    'Time of day':
    'Past sunset but not dark yet',
    'description':
    'I am in a vast hard but deserty land. Pople are running away from something. I ran with them. They ran towards some wodden shelters which are very large. A giant monter is apporaching.'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', dreams=dreams)


@app.route('/api/dreams')
def list_of_dreams():
  return jsonify(dreams)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
