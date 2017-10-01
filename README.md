# todoist-imdb
Automatically add IMDB rating and description to movies listed on todoist.

![Imgur](https://i.imgur.com/DNE91TF.png)

## Usage
1. Install required dependancies
```
pip install -r requirements.txt
```

2. Get todoist API key from settings > integrations on [todoist.com](https://todoist.com).

3. Set the API key as environment variable named
```
export TODOIST_APIKEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

4. Schedule the script to run periodically.
```
python movierater.py
```
