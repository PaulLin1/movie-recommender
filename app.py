from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database/main.db')
    return conn

def add_like():
    conn = get_db()

def clear_likes():
    conn = get_db()

@app.route('/')
def home():
    conn = get_db()
    movies = conn.execute('SELECT * FROM movielens ORDER BY RANDOM() LIMIT 15').fetchall() # Gets 15 random movies
    return render_template('index.html', movies=movies)

@app.route('/profile')
def profile():
    conn = get_db()
    likes = conn.execute('SELECT title FROM likes').fetchall() # Gets all of the profile's likes

    return render_template('profile.html', likes=likes)

@app.route('/item/<int:item_id>')
def item_page(item_id):
    conn = get_db()
    movie_info = conn.execute('SELECT * FROM movielens WHERE id = ?', (item_id,)).fetchall()[0] # Gets selected movie's info
    recommendations = conn.execute('SELECT * FROM movielens ORDER BY RANDOM() LIMIT 5').fetchall() # Gets 5 random 'recommendations'

    return render_template('item_page.html', movie_info=movie_info, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
