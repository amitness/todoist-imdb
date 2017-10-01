#!/usr/bin/env python

import os
import requests
from pytodoist import todoist

MOVIES_PROJECT = 'Movies'


def get_token():
    token = os.getenv('TODOIST_APIKEY')
    return token


def get_details(movie_name):
    base_url = 'http://theapache64.xyz:8080/movie_db/search?keyword={}'
    url = base_url.format(movie_name)
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        error = r.json()['error']
        if not error:
            print r.json()
            return r.json()['data']


def add_details(tasks):
    for task in tasks:
        if '.' in task.content[-7:-2]:
            continue
        data = get_details(task.content)
        if data:
            rating = data.get('rating', 0.0)
            imdb_id = data['imdb_id']
            plot = data['plot']
            imdb_url = 'http://www.imdb.com/title/{}'.format(imdb_id)
            task_format = '**[{}]({})** | {} | **({})**'
            task.content = task_format.format(task.content,
                                              imdb_url, plot, rating)
            task.update()


def main():
    API_TOKEN = get_token()
    if not API_TOKEN:
        print "Please set the API token in environment variable."
        exit()
    user = todoist.login_with_api_token(API_TOKEN)
    movies = user.get_project(MOVIES_PROJECT)
    tasks = movies.get_tasks()
    add_details(tasks)

if __name__ == '__main__':
    main()
