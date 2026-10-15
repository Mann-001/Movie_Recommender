# 🎬 Movie Recommender System

A Content-Based Movie Recommender System that suggests movies similar to your favorite choices. The application leverages Natural Language Processing (NLP) and vectorization to understand the context of movies and recommends the top 5 most similar films, complete with real-time posters fetched via the TMDB API.

🔴 **Live Demo:** [https://movie-recommender-sdi7.onrender.com](https://movie-recommender-sdi7.onrender.com)  
*(Note: As this is hosted on a free Render tier, it may take ~50 seconds to spin up if it has been inactive).*

---

##  Features
* **Smart Recommendations:** Recommends 5 highly similar movies based on input.
* **Real-Time Visuals:** Integrates with the TMDB API to fetch high-quality movie posters on the fly.
* **Interactive UI:** Clean, user-friendly web interface built entirely in Python using Streamlit.

---

##  How It Works (Under the Hood)

This system uses a **Content-Based Filtering** approach. Instead of looking at user ratings, it analyzes the actual metadata of the movies (Genres, Keywords, Cast, Director, and Overview) to find similarities.

### 1. Data Cleaning & Analytics
* Merged the **TMDB 5000 Movies** and **TMDB 5000 Credits** datasets.
* Extracted relevant features from complex JSON-like dictionary structures (e.g., pulling the top 3 actors from the cast list and isolating the director from the crew).
* Cleaned the data by removing spaces between names (e.g., `Sam Worthington` → `SamWorthington`) to ensure the machine treats individual people as unique entities rather than overlapping dictionary words.

### 2. Natural Language Processing (NLP)
* Merged all metadata into a single string of `tags` for each movie.
* Applied **Stemming** using NLTK's `PorterStemmer` to reduce words to their root forms (e.g., transforming "actions", "acting", and "actor" all down to the root word "act") to prevent feature duplication.

### 3. Text Vectorization
* Converted the raw text `tags` into mathematical vectors using the **Bag of Words (BoW)** technique via `CountVectorizer`.
* Limited the vocabulary to the top 5,000 most frequently used words across all movies.
* Removed English "stop words" (like *and, the, is, are*) that carry no analytical value.

### 4. Similarity Calculation
* Calculated the **Cosine Similarity** between all 4,800+ movie vectors in a 5000-dimensional space.
* The system measures the angle between vectors (where a smaller angle implies higher similarity) to instantly rank and return the closest matches.

---

##  Tech Stack

* **Data Science & ML:** Pandas, NumPy, Scikit-Learn (CountVectorizer, Cosine Similarity), NLTK (PorterStemmer)
* **Web Framework:** Streamlit
* **API Integration:** Requests (TMDB API)
* **Deployment:** Render (with GitHub integration)
* **Compression:** Python `bz2` (for large Pickle file handling)

---

##  Run It Locally

If you want to clone this repository and run it on your own machine:

**. Clone the repository:**
```bash
git clone [https://github.com/Mann-001/Movie_Recommender.git](https://github.com/Mann-001/Movie_Recommender.git)
cd Movie_Recommender
