from app import app
from flask import url_for, flash, render_template, redirect, request
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
	return "Hello world!"