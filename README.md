# todoist-imdb
Automatically add IMDB rating and description to movies listed on todoist.

![Imgur](https://i.imgur.com/DNE91TF.png)

The script adds IMDB link, rating and description to the task in project *Movies*.


## Usage
1. Create a project "Movies" on todoist.

2. Install required dependancies.
    ```
    pip install -r requirements.txt
    ```

3. Get API key from `Settings > integrations` on [https://todoist.com](https://todoist.com).

4. Set the API key as environment variable.
    ```
    export TODOIST_APIKEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ```

5. Schedule the script to run periodically.
    ```
    python movierater.py
    ```
