import requests
import json
import sys


class Repository:

    def __init__(self, id, name, description, url, language, watchers_count):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.language = language
        self.watchers_count = watchers_count

    def __str__(self):
        delimiter = "=" * 40
        return "ID: %s\nNAME: %s\nDESCRIPTION: %s\nURL: %s\nLANGUAGE: %s\nWATCHERS_COUNT: %s\n%s" % (
            self.id, self.name, self.description, self.url, self.language, self.watchers_count, delimiter)


class RepositoryService:

    def __init__(self):
        self.listOfRepositories = []

    def fetchData(self, user, token):
        response = requests.get("https://api.github.com/users/" + user + "/repos", headers={'Authorization': token})
        if response.status_code == 200:
            print("Status code was OK")
            print("List of repositories were fetched successfully\n")
        elif response.status_code == 404:
            print("Status code was NOT_FOUND")
            print("Username doesn't exist\n")
            exit()
        parsed = json.loads(response.content)
        for data in parsed:
            self.listOfRepositories.append(
                Repository(data["id"], data["name"], data["description"], data["url"], data["language"],
                           data["watchers_count"]))


def main():
    TOKEN = "172d3a596f9cd5adf66b37065b54db091077b23b"
    args = sys.argv
    if len(args) == 1:
        print("Please add username as command line argument")
    else:
        username = sys.argv[1]
        service = RepositoryService()
        service.fetchData(username, TOKEN)
        for repo in service.listOfRepositories:
            print(repo)


main()
