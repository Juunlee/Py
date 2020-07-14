from tools.node import Node

AL = Node("Austronesian lang")

Formosan = Node("Formosan")
AL.insert_left(Formosan)

MP = Node("Malayo Polynesian")
AL.insert_right(MP)

NorthernF = Node("NorthernF")
Formosan.insert_left(NorthernF)

EastF = Node("EasternF")
Formosan.insert_right(EastF)

Atayalic = Node("Atayalic")
NorthernF.insert_left(Atayalic)

NorthWestF = Node("NorthWestF")
NorthernF.insert_right(NorthWestF)

Kavalanic = Node("Kavalanic")
EastF.insert_left(Kavalanic)

Ami = Node("Ami")
EastF.insert_right(Ami)

WesternMP = Node("WesternMP")
MP.insert_left(WesternMP)

CEMP = Node("Central-EasternMP")
MP.insert_right(CEMP)

Philippine = Node("Philippine")
WesternMP.insert_left(Philippine)

SamBaj = Node("Sama-Bajaw")
WesternMP.insert_right(SamBaj)

SuFl = Node("Sumb-Flores")
CEMP.insert_left(SuFl)

Oceanic = Node("Oceanic")
CEMP.insert_right(Oceanic)
