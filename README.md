# 🎬 Smart Movie Recommendation System
A content-based movie recommendation web app — enter a movie title and get instant similar movie suggestions.

## 🎥 Demo
[![LinkedIn Demo Video](https://img.shields.io/badge/Watch%20Demo-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/feed/update/urn:li:activity:7461709773860679681/)

> 📽️ Watch the full demo on LinkedIn — live movie recommendations in action!

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
**Indunil Udayanga**  
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Indunil-Udayanga/smart-movie-recommendation-system)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/feed/update/urn:li:activity:7461709773860679681/)
