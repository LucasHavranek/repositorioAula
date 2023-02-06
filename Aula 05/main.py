from flask import Flask, redirect, url_for, request, render_template
import requests
import json, requests

app = Flask(__name__)


@app.route('/')
def inicio():
  return render_template('home.html')


@app.route('/login/')
def login():
  return render_template('login.html')


@app.route('/404/')
def error404():
  return render_template('404.html')


@app.route('/check/', methods=['POST'])
def check():
  if request.method == 'POST':
    user = request.form['c_usuario']
    password = request.form['c_senha']
    if user == '123' and password == '123':
      return redirect(url_for('membros'))
    else:
      return redirect(url_for('404'))


@app.route('/membros/')
def membros():
  text = "Login successful"
  return text


if __name__ == '__main__':
  app.run('0.0.0.0')
