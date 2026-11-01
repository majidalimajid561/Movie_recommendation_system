# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-darkblue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0%2B-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)

A **Content-Based Movie Recommendation System** that suggests movies similar to a selected title based on movie metadata (genres, keywords, cast, crew, and overview).

## 📖 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [ML Development Pipeline](#ml-development-pipeline)
- [Recommendation Approach](#recommendation-approach)
- [Application Flow](#application-flow)
- [Technologies Used](#technologies-used)
- [How to Run Locally](#how-to-run-locally)
- [Author](#author)

---

## 🔍 Overview
Finding a good movie to watch can be time-consuming. This project solves that by recommending movies based on the **content** of a movie the user already enjoys. By analyzing features like genre, cast, and plot overview, the system finds and ranks the most similar movies.

## 🎯 Problem Statement & Objective
**Problem:** Users often struggle to find new movies that match their specific tastes.
**Objective:** Given a movie title, recommend the top-N most similar movies using Content-Based Filtering.

## 📊 Dataset
The model is trained on a movie dataset containing **4,806 movies**. 
Key features used for text vectorization include:
- Movie Title
- Genres
- Keywords
- Plot Overview
- Top Cast
- Director / Crew

## ⚙️ ML Development Pipeline

```text
📁 Raw Movie Dataset
      ↓
🧹 Data Cleaning (Handling missing values, formatting)
      ↓
🛠️ Feature Engineering (Extracting top 3 cast, crew, etc.)
      ↓
🔗 Feature Combination (Merging all text into one "tag" column)
      ↓
🔢 Text Vectorization (Bag of Words / CountVectorizer)
      ↓
📐 Cosine Similarity (Calculating distance between vectors)
      ↓
💾 Saved Recommendation Artifacts (.pkl files)
```
---


## 🚀 Application Flow

1. User Input: User selects a movie from the Streamlit dropdown.

2. Search: The app finds the movie's index in the dataset.

3. This show the top five similar  movies

---

## 💻 Technologies Used
- Language: Python

- Data Manipulation: Pandas, NumPy

- Machine Learning: Scikit-Learn (CountVectorizer, Cosine Similarity)

- Frontend Web App: Streamlit

- Model Serialization: Pickle

---

## 🏃‍♂️ How to Run Locally
1. Clone the repository

``` bash
git clone https://github.com/majidalimajid561/Movie_recommendation_system
cd Movie-Recommendation-System

```
``` bash
2. Create and activate a virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit App

streamlit run app.py
```


### 👨‍💻 Author
- Majid Mehmood

- GitHub: @majidalimajid561

- LinkedIn: [Your LinkedIn Here]

If you like this project, please give it a ⭐!