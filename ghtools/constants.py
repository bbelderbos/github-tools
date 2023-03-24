from decouple import config

GH_TOKEN = config("GITHUB_REPO_TOKEN")
GH_USER = config("REPO_OWNER")
SOURCE_REPO = config("SOURCE_REPO", default=None)
DESTINATION_REPO = config("DESTINATION_REPO", default=None)
OPEN_STATUS = "open"
