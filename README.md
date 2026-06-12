# Movie Recommendation System

A movie recommendation web application built using the MovieLens dataset.  
The system recommends movies similar to a selected movie using item-based collaborative filtering and cosine similarity.

## Project Overview

This project analyzes user movie ratings and builds a recommendation system that suggests similar movies based on user rating patterns.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook
- Git and GitHub

## Dataset

Dataset: MovieLens Latest Small Dataset

The dataset contains:
- Movie information
- User ratings
- Movie genres

Main files used:
- `movies.csv`
- `ratings.csv`

## Methodology

1. Loaded and explored the MovieLens dataset.
2. Performed exploratory data analysis on ratings and movie popularity.
3. Created a user-movie matrix.
4. Calculated movie similarities using cosine similarity.
5. Built an item-based collaborative filtering recommendation engine.
6. Developed a Streamlit web application for user interaction.

## Features

- Search movie by title
- Generate similar movie recommendations
- Display movie genres
- Display similarity scores
- Interactive Streamlit interface

## How to Run the Project

Install dependencies:

```bash
pip install -r requirements.txt