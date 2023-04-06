import os
from tqdm.gui import trange

from flask import Blueprint, render_template, request, Flask, flash, send_file
import pandas as pd
from flask_login import login_user, login_required, logout_user, current_user

from .summarizer import getSummary
from .audioprocessing import getTranscript
from .LSTM.NeuralNet.videoprocessing import getVideoCaptions
from .data import text
 
# Data Processing
import numpy as np
import pandas as pd

from website.models import User

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
  info = "Summarization done"
  category = "success"
  summary = "--"
  captions = " "
  transcript = " "

  if request.method == 'POST':
    file = request.files['vid']
    name = file.filename
    name = name.split('.')[0]
    file.save(os.path.join('D:/SEM-6/E1_NLP ()/Project/proj/uploaded/', file.filename))
    
    transcript = getTranscript(name)
    captions = getVideoCaptions('D:/SEM-6/E1_NLP ()/Project/proj/uploaded/' + file.filename)
    summary = getSummary(captions + " \n " + transcript)

    flash(info, category=category)    
  return render_template('home.html', summary = summary, captions = captions, transcript = transcript)

@views.route('/help')
def help():
    return render_template('help.html')

@views.route('/data', methods=['GET', 'POST'])
def data():
  length_users = 0
  users =  User.query.order_by(User.id).all()
  if users:
      length_users = len(users)
      return render_template("data.html", users = users, len = length_users)
