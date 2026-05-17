from flask import Flask, render_template, request, redirect, url_for
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "movie_recommender.pkl")

try:
    with open(file_path, "rb") as f:
        data = pickle.load(f)

    df = data["movies"].reset_index(drop=True)
    similarity = data["similarity"]

    # Normalize duration column — support both 'Runtime' and 'Duration'
    if 'Runtime' in df.columns and 'Duration' not in df.columns:
        df.rename(columns={'Runtime': 'Duration'}, inplace=True)

    # Clean up: strip " min" suffix if present (e.g. "130 min" → "130")
    if 'Duration' in df.columns:
        df['Duration'] = df['Duration'].astype(str).str.replace(r'\s*min.*', '', regex=True).str.strip()
        df['Duration'] = df['Duration'].replace({'nan': '', 'None': '', 'NaN': ''})

    print("✅ Model loaded")

except Exception as e:
    print("❌ Error:", e)
    df = None
    similarity = None


# Recommend Function
def recommend(movie_name):
    movie_name = movie_name.strip().lower()

    if df is None:
        return None, []

    matches = df[df['Title'].str.lower().str.contains(movie_name, na=False)]

    if matches.empty:
        return None, []

    idx = matches.index[0]

    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:11]

    recs = []
    for i, score in distances:
        row = df.iloc[i].to_dict()
        row['Score'] = round(float(score), 3)
        recs.append(row)

    return df.iloc[idx].to_dict(), recs


# Home
@app.route('/')
def home():
    categories = [
        "Action", "Comedy", "Drama", "Romance",
        "Thriller", "Horror", "Adventure",
        "Sci-Fi", "Fantasy", "Crime",
        "Animation", "Mystery"
    ]
    return render_template("index.html", categories=categories)


# Search
@app.route('/search', methods=['POST'])
def search():
    movie = request.form.get('movie', '').strip()

    if not movie:
        return redirect('/')

    selected, recs = recommend(movie)

    if selected is None:
        return render_template("results.html",
                               error=f'No results found for "{movie}". Try another title.')

    return render_template("results.html",
                           movie=selected,
                           recommendations=recs)


# Category
@app.route('/category/<cat>')
def category(cat):
    if df is None:
        return render_template("results.html", error="Data not loaded.")

    filtered = df[df['Genres'].str.contains(cat, case=False, na=False)].head(20)

    return render_template("results.html",
                           category=cat,
                           recommendations=filtered.to_dict(orient='records'))


if __name__ == "__main__":
    app.run(debug=True)