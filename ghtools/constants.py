from decouple import config

GH_TOKEN = config("GITHUB_REPO_TOKEN")
GH_USER = config("REPO_OWNER")
SOURCE_REPO = config("TEMPLATE_REPO")
OPEN_STATUS = "open"
