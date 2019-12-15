from flask import Flask, render_template, request, jsonify
from forms import *
import json
import requests
import unidecode
import random
import time

app=Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

def find_title(clusters, title):
    for key in clusters.keys():
        for i, member in enumerate(clusters[key]['members']):
            if member == title:
                return i, clusters[key]

    return None, None


def get_idxs(cluster, pos):
    nr_elems = len(cluster['members'])

    if (nr_elems == 1):
        return 'Nu exista stiri similare', 'Nu exista stiri similare'

    random.seed(time.clock())
    
    idxs = [i for i in range(nr_elems) if i != pos]
    idx_1 = random.choice(idxs)
    first = cluster['urls'][idx_1]

    if (nr_elems > 2):
        idxs.remove(idx_1)
        idx_2 = random.choice(idxs)
        second = cluster['urls'][idx_2]
    else:
        second = 'Nu mai exista alte stiri similare'

    return first, second


def get_more(clusters, category, pos):
    idxs = []
    for key in clusters.keys():
        cluster = clusters[key]
        if cluster['idx'] != pos:
            if cluster['category'] == category:
                idxs.append(cluster['idx'])

    random.seed(len(idxs))
    idx_1 = random.choice(idxs)
    
    idxs.remove(idx_1)
    idx_2 = random.choice(idxs)

    url1 = clusters[str(idx_1)]['urls'][random.choice([i for i in range(clusters[str(idx_1)]['len'])])]
    url2 = clusters[str(idx_2)]['urls'][random.choice([i for i in range(clusters[str(idx_2)]['len'])])]

    return url1, url2


@app.route('/', methods=['GET', 'POST'])
def recommend_article():
    form = RecommendForm()
    with open('frontend.json') as json_file:
        clusters = json.load(json_file)
    
    if form.validate_on_submit():
        if 'recommend' in request.form:
            form.recommended_1.data = ''
            form.recommended_2.data = ''
            form.more_recommended_1.data = ''
            form.more_recommended_2.data = ''
           
            title = form.article_title.data
          
            pos, cluster = find_title(clusters, title)
            url1, url2 = get_idxs(cluster, pos)

            form.recommended_1.data = url1
            form.recommended_2.data = url2
        
            more_1, more_2 = get_more(clusters, cluster['category'], pos)
            form.more_recommended_1.data = more_1
            form.more_recommended_2.data = more_2


    return render_template('recommend.html', 
                            title='Recommend article', 
                            form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

