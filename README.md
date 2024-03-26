# Twitter Crawler Project
[中文版](README_CN.md)


This project contains two main scripts for scraping tweets from Twitter: `set_cookies.py` and `spyder.ipynb`.

## set_cookies.py

- Purpose: Automates the process of logging into Twitter and saving the login cookies.
- How it works: Opens the Twitter login page and waits for the user to log in manually. After 30 seconds, it saves the session cookies into a file.

## spyder.ipynb

- Purpose: Uses the saved cookies to scrape tweets from a specified Twitter search URL.
- Features: Loads cookies, navigates to a Twitter search page, collects tweets, extracts details (username, text, images), and saves the data to a JSON file.

## Installation

Ensure you have Python and Selenium installed. You may need to adjust the path to your ChromeDriver in both scripts.

## Usage

1. Run `set_cookies.py` first to log in and save your cookies.
2. Modify the search URL in `spyder.ipynb` as needed.
3. Run `spyder.ipynb` to start scraping tweets.



