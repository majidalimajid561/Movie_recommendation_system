# Movie Recommendation System

## 1. Overview

A content-based movie recommendation system that recommends
movies similar to a selected movie.

## 2. Problem Statement

Users often have difficulty finding movies similar to ones
they already enjoy.

This project recommends movies based on movie content.

## 3. Objective

Given a movie, recommend the most similar movies.

## 4. Dataset

Movie dataset containing information such as:

- Movie title
- Genres
- Keywords
- Overview
- Cast
- crew
and 4806 mvies.


## ML Development Pipeline

How did I build the recommendation system?

Raw Movie Dataset
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Feature Combination
        ↓
Text Vectorization
        ↓
Cosine Similarity
        ↓
Saved Recommendation Artifacts

## Application Flow

1.User selects movie 

2.Streamlit application 

3.Find movie in dataset 

4.Retrieve similarity scores

5.Rank similar movies 

6.Top-N recommendations 

7.Display to user


##  Recommendation Approach

This project uses Content-Based Filtering.

Movies are recommended based on similarity between their
content/features rather than other users' behavior.

## 🏃‍♂️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/majidalimajid561/house-price-predictor.git
   cd house-price-predictor

2. Create a virtual environment
python -m venv venv
source venv/bin/activate

3. pip install -r requirements.txt

4. streamlit run.py


##  Technologies
numpy
Python
Pandas
Scikit-learn
Streamlit


##  Author

Majid Mehmood