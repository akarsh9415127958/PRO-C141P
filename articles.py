from crypt import methods
from flask import Flask, jsonify,request
import csv

all_articles = []

with open("articles.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_like = []

app = Flask(__name__)
@app.route("/get-articles")

def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    }),201

@app.route("/like-article",
methods = ["post"])

def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/not-like-article",
methods = ["post"])

def not_liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did-not-like",
methods = ["post"])

def did_not_like_article():
    article = all_articles[0]
    all_movies = all_articles[1:]
    did_not_like.append(article)
    return jsonify({
        "status":"success"
    }),201

