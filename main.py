import numpy as np
import pandas as pd
from flask import Flask,render_template,request,url_for
from sklearn.neighbors import NearestNeighbors
import pickle as pkl

with open('C:/Users/Mnight/knn1000.pickle','rb') as fin:
	knn=pkl.load(fin)

dfsub=pd.read_csv('C:/Users/Mnight/subreddit_info.csv')
subfeat=pd.read_csv('C:/Users/Mnight/subredditfeats1000.csv')

def getsubrecs(x):
    ind=subfeat[subfeat.subreddit==x].index[0]
    dis,inds=knn.kneighbors(subfeat.iloc[ind].values[1:].reshape(1,-1),n_neighbors=int(5))
    a={subfeat.iloc[subfeat.index[inds.flatten()[i]]]['subreddit']:dfsub[dfsub.subreddit==subfeat.iloc[subfeat.index[inds.flatten()[i]]]['subreddit']]['public_description'].values[0] for i in range(len(dis.flatten()))}
    return a

app=Flask(__name__)

@app.route('/')
@app.route('/home',methods=['GET'])
def home():
	return render_template('home.html')


@app.route('/recommend',methods=['POST'])
def recommend():
	sb=request.form['subred']
	if sb not in subfeat['subreddit'].unique():
		return render_template('404.html')
	pack=getsubrecs(sb)
	return render_template('recommend.html',pack=pack)

@app.route('/sugg',methods=['POST'])
def sugg():
	sb=request.form.get('clkbtn')
	pk=getsubrecs(sb)
	return render_template('recommend.html', pack=pk)


if __name__=='__main__':
	app.run(debug=True)
