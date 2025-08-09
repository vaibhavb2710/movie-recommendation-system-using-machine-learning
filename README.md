# movie-recommendation-system-using-machine-learning
A content-based Movie Recommendation System built with Python, Machine Learning, and Streamlit. Recommends similar movies based on genres, cast, and descriptions, with poster fetching via TMDB API.

# 🎬 Movie Recommendation System using Machine Learning

This project is a **Movie Recommendation System** built using **Python**, **Machine Learning**, and **Streamlit**.  
It recommends movies based on similarity scores computed from their features (like genres, cast, and descriptions).
📌 Features
- **Content-based filtering** to recommend similar movies.
- **Streamlit web app** for an interactive UI.
- Uses **TMDB API** to fetch movie posters.
- Well-structured code with modular design.
- Deployed using **Heroku** (or can be deployed locally).
📂 Project Structure
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── Movie Recommender System Data Analysis.ipynb # Data exploration & preprocessing
├── src/ # Utility functions and helpers
├── data/ # Raw data files (if any)
├── artifacts/ # Saved ML models & processed data
├── demo/ # Screenshots of the app
├── setup.py # Package setup file
├── setup.sh # Shell script for deployment
├── Procfile # Heroku deployment config
├── LICENSE # License file
└── README.md # Project documentation

🚀 Installation & Setup
1. Clone the repository
```bash
git clone https://github.com/your-username/movie-recommendation-system-ml.git
cd movie-recommendation-system-ml
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the application

bash
Copy
Edit
streamlit run app.py
Access the app
Go to http://localhost:8501 in your browser.

🛠️ How It Works
Data Preprocessing:

Reads movie dataset.

Extracts relevant features (overview, genre, cast, crew).

Cleans and tokenizes data.

Feature Extraction:

Converts text data into vectors using CountVectorizer.

Calculates similarity scores using cosine similarity.

Recommendation:

When a user selects a movie, the system finds the most similar movies.

Displays top recommendations with posters fetched via TMDB API.

📸 Demo
Here are some screenshots of the app:
<img width="789" height="839" alt="image" src="https://github.com/user-attachments/assets/c2847565-22cd-495d-a3ac-c972ae921018" />

📦 Requirements
The main dependencies are:
nginx
Copy
Edit
streamlit
pandas
numpy
scikit-learn
requests
Full list in requirements.txt.

🔗 API Key Setup
This project uses the TMDB API for fetching movie posters.
Create an account on TMDB.
Go to Settings → API → Request API Key.
Replace YOUR_API_KEY in app.py with your API key.

👨‍💻 Author
Developed by Vaibhav Bedre
Feel free to fork this project and improve it! 🚀
