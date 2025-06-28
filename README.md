# 🎬 Movie Recommendation System

A simple yet powerful **Content-Based Movie Recommendation System** that suggests similar movies using **cosine similarity** and **NLP preprocessing**.

---

## 📌 Project Objective

> **Goal:** Recommend movies that are similar to a selected movie title based on the plot, genre, keywords, and other text features — using **text vectorization** and **cosine similarity**.

---

## 📂 Dataset

- 📥 **Source:** [Kaggle](https://www.kaggle.com/) — e.g., TMDB or IMDb dataset
- Columns include:
  - **Title**
  - **Genres**
  - **Plot / Overview**
  - **Keywords**
  - **Cast / Crew**

---

## 🧩 Approach

- 📚 **NLP Preprocessing:** 
  - Tokenization, stopword removal, stemming with **NLTK**
  - Combined relevant text fields into a single **“tags”** feature
- 🧮 **Vectorization:** 
  - Converted text data into numeric vectors using **CountVectorizer** or **TF-IDF**
- 🔗 **Similarity Metric:** 
  - Calculated **cosine similarity** across all movies
- 🎥 **Recommendation:** 
  - Recommend top N most similar movies based on similarity scores

---

## ⚙️ Highlights

- ✅ No supervised ML model — purely **content-based filtering**
- ⚡ Fast similarity search using pre-computed vectors
- 🗂️ Easy to expand with more metadata (e.g., director, ratings)
- 📌 Built with clean, modular Python code for reuse

---

## 🚀 How to Run Locally

1️⃣ **Clone the repo**
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
