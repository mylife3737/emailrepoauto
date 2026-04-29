import requests

def get_trending_ai():
    # Searching for AI repos with >1000 stars, sorted by most recently updated
    url = "https://api.github.com/search/repositories?q=topic:ai+stars:>1000&sort=updated&order=desc"
    response = requests.get(url)
    repos = response.json().get('items', [])[:10]
    
    with open("AITrends.md", "w") as f:
        f.write("# Trending AI Repositories\n\n")
        f.write("| Name | Description | Stars | Link |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for repo in repos:
            f.write(f"| {repo['name']} | {repo['description']} | {repo['stargazers_count']} | [Link]({repo['html_url']}) |\n")

if __name__ == "__main__":
    get_trending_ai()
    print("AITrends.md has been generated successfully!")
