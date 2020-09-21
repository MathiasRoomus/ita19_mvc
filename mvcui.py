from view import View
from model import Model
from controller import Controller

kaubad = [
    {"nimetus": "leib", "hind":0.80, "kogus": 20},
    {"nimetus": "piim", "hind":0.50, "kogus": 15},
    {"nimetus": "vein", "hind":5.60, "kogus": 5},
]

pood = Controller(Model(kaubad), View())

pood.kuva_elemendid()
pood.kuva_element("vein on")