# 🎬 Smart Movie Recommendation System

A content-based movie recommendation web app — enter a movie title and get instant similar movie suggestions.

## Tech Stack
`Python` `Flask` `Scikit-learn` `HTML/CSS`

## How It Works
Movie features (description, genre, director, writer) are vectorized using **TF-IDF** and matched via **Cosine Similarity** across a dataset of ~16,000 movies. The trained model is served through a Flask web app.

## Run Locally
```bash
pip install flask scikit-learn pandas numpy
cd recomendation_app
python app.py
```
Open `http://127.0.0.1:5000` — make sure `movie_recommender.pkl` is in the same folder as `app.py`.

## Author
**Indunil Udayanga** · [GitHub](https://github.com/Indunil-Udayanga/smart-movie-recommendation-system)
