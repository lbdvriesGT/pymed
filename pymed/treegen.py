import requests
import re

BASE_URL = "https://meshb.nlm.nih.gov/record/ui?ui="


def getTree(mesh_id):
    tree = []
    response = requests.get(
        f'https://meshb.nlm.nih.gov/api/record/ui/{mesh_id}')
    for object in response.json()["TreeNumberList"]["TreeNumber"]:
        tree.append(object["t"])
    return tree


def mainDescriptors(mesh_id):
    p = (re.compile('[A-Z | a-z]\w+'))
    tree = []
    response = requests.get(
        f'https://meshb.nlm.nih.gov/api/record/ui/{mesh_id}')
    for object in response.json()["TreeNumberList"]["TreeNumber"]:
        if p.findall(object["t"])[0] not in tree:
            tree.append(p.findall(object["t"])[0])
    return tree
