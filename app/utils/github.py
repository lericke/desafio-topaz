import requests


class Github:
    
    def get_data(self, username):


        github_url = f"https://api.github.com/users/{username}"

        user_data = requests.get(github_url).json()

        return user_data

    def get_repos(self, username):


        github_url = f"https://api.github.com/users/{username}"

        user_repos = requests.get(github_url+"/repos").json()
        
        return user_repos