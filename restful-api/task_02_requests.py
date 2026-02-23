#!/usr/bin/python3

"""Pull a json out of thin air and do stuff with it"""
import requests, csv


def fetch_and_print_posts():
    """Fetch and print them!"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post)
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    """Now we get to save it"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        #  Structure the posts to the keys
        structured_posts = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
             for post in posts ]

        #  Write to CSV
        with open('posts.csv', 'w', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)

        print("Posts saved to posts.csv successfully!")
    
    else:
        print("Failed to fetch posts.")

fetch_and_print_posts()