# 0x16. API Advanced - Reddit API Exploration

This project delves into the Reddit API, showcasing various techniques for interacting with and extracting information from this popular social media platform. 

## Project Overview

The scripts in this repository focus on:

- Fetching the number of subscribers for a given subreddit.
- Retrieving and printing the titles of the top 10 hot posts in a subreddit.
- Recursively collecting the titles of all hot posts within a subreddit.
- Recursively counting and ranking keywords within the titles of hot posts in a subreddit.

## Files

* **0-subs.py:**
    - Function: `number_of_subscribers(subreddit)`
    - Description: Queries the Reddit API to retrieve the total subscriber count for a specified subreddit.
    - Returns: The number of subscribers (int), or 0 if the subreddit is invalid.

* **1-top_ten.py:**
    - Function: `top_ten(subreddit)`
    - Description: Fetches and prints the titles of the top 10 hottest posts in a subreddit.
    - Output: Prints the titles to the console, or "None" if the subreddit is invalid.

* **2-recurse.py:**
    - Function: `recurse(subreddit, hot_list=[])`
    - Description: Recursively explores the Reddit API to gather the titles of all hot posts in a subreddit.
    - Returns: A list of post titles (list), or `None` if none are found or the subreddit is invalid.

* **100-count.py:**
    - Function: `count_words(subreddit, word_list)`
    - Description: Recursively analyzes hot posts in a subreddit, counting the frequency of keywords from `word_list` in post titles.
    - Output: Prints a sorted list of keywords with their counts in descending order.

* **0-main.py, 1-main.py, 2-main.py, 100-main.py:**
    - Description: Sample scripts to demonstrate how to use the functions defined in the corresponding .py files. These scripts take subreddit names and/or keyword lists as command-line arguments.

## Requirements

- **Python 3.4.3:** This project is specifically designed for Python version 3.4.3.
- **Requests Library:** Install it via `pip install requests`.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone [invalid URL removed]
    cd 0x16-api_advanced
    ```

2. **Run Scripts:**
    - Execute the main scripts (e.g., `./0-main.py programming`) to test each function. Make sure to replace `programming` with the subreddit you want to query.
    - For `100-main.py`, provide a list of keywords as a space-separated string:
       ```bash
       ./100-main.py programming "python java javascript"
       ```

## Key Considerations

- **User-Agent Header:** Each request sets a custom `User-Agent` to avoid being rate-limited by the Reddit API.  
- **Error Handling:** The scripts include checks for invalid subreddits and potential API errors.
- **Recursion:** The `recurse` and `count_words` functions demonstrate the use of recursion to navigate the API's pagination and process all available results.
- **Sorting and Filtering:** `count_words` implements a sorting algorithm to display the keyword counts in a user-friendly manner.

## Disclaimer

The examples and numbers used in this project may not be accurate in the future as Reddit's content is constantly changing.
