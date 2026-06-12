#!/usr/bin/python3
"""Fetches and processes posts from the JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches all posts and saves them into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post.get("id"),
             "title": post.get("title"),
             "body": post.get("body")}
            for post in posts
        ]
        with open("posts.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
