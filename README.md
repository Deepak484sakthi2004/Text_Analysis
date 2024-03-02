# Text Analysis App

Welcome to the Text Analysis App! This application allows you to perform various text analysis tasks using Google Gemini API for context generation, keyword extraction, and word prompting. It also includes functionality for extracting key points, identifying most positive words, and generating word clouds. The app is deployed on a free Heroku server.

## Table of Contents
- [Getting Started](#getting-started)
- [Features](#features)
  - [Context Generation](#context-generation)
  - [Keyword Extraction](#keyword-extraction)
  - [Key Points Extraction](#key-points-extraction)
  - [Most Positive Words](#most-positive-words)
  - [Word Cloud Generation](#word-cloud-generation)
  - [Entity Recognition](#entity-recognition)
- [Deployment](#deployment)
- [Usage](#usage)
- [Limitations](#limitations)
- [Comic Note](#comic-note)

## Getting Started

To use the Text Analysis App locally, follow these steps:

Feel free to explore, analyze, and have fun with the Text Analysis App!
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-analysis-app.git
2. Install dependencies:
     ```bash
     pip install -r requirements.txt
3. Run the Streamlit app:
  ```bash
    streamlit run app.py
  ```

# Text Analysis App

Welcome to the Text Analysis App! This application allows you to perform various text analysis tasks using Google Gemini API for context generation, keyword extraction, and word prompting. It also includes functionality for extracting key points, identifying most positive words, and generating word clouds. The app is deployed on a free Heroku server.

## Features

### Context Generation
The app uses Google Gemini API to generate context around a given text. It helps in understanding the context in which a particular keyword is used.

### Keyword Extraction
Utilizing the power of Google Gemini API, the app extracts keywords from the provided text, helping to identify important terms.

### Key Points Extraction
The `extract_key_points` function extracts key points from the text, summarizing the main ideas and concepts.

### Most Positive Words
Using sentiment analysis, the app identifies and lists the most positive words in the input text.

### Word Cloud Generation
The `generate_wordcloud` function creates a visually appealing word cloud based on the frequency of words in the text, providing a quick overview of the content.

### Entity Recognition
Spacy is used for Named Entity Recognition (NER), identifying entities such as persons, organizations, and locations in the text.

## Deployment
The Text Analysis App is deployed on a free Heroku server. You can access the live app [here](https://text-analysis-poa5.onrender.com/).

## Usage
1. Enter the text you want to analyze in the provided input box.
2. Choose the desired analysis option from the sidebar.
3. Explore the generated insights and visualizations.

## Limitations
Please note that the Google Gemini API has a limitation of 60 calls per minute. Ensure that your usage doesn't exceed this limit to avoid interruptions in service.

## Comic Note
🚨 Comic Note: Don't go more than 60 clicks for a minute! 🚨
Be cautious with your usage, as the Google Gemini API has a limit on the number of calls you can make within a minute. Stay within the prescribed limit to keep the analysis flowing smoothly!

