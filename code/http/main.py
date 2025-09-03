import requests
import json

res = requests.get("https://jsonplaceholder.typicode.com/posts")
if not res.ok:
    print("Error", res.content)
    exit()

posts = res.json()

print(f"Total Posts: {len(posts)}")


with open('posts.json', 'w+', encoding="utf-8") as f:
    f.write(json.dumps(posts))
