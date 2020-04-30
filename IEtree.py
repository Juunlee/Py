from tools.node import Node

PIH = Node("PIH")

PIE = Node("PIE")
PIH.insert_left(PIE)

Anatolian = Node("Anatolian")
PIH.insert_right(Anatolian)

MIE = Node("MIE")
PIE.insert_left(MIE)

Tocharian = Node("Tocharian")
PIE.insert_right(Tocharian)

Luwian = Node("Luwian")
Anatolian.insert_left(Luwian)

Hittite = Node("Hittite")
Anatolian.insert_right(Hittite)

LIE = Node("LIE")
MIE.insert_left(LIE)

Germanic = Node("Germanic")
MIE.insert_right(Germanic)

A = Node("A")
Tocharian.insert_left(A)

B = Node("B")
Tocharian.insert_right(B)

Lydian = Node("Lydian")
Luwian.insert_left(Lydian)

Lycian = Node("Lycian")
Luwian.insert_right(Lycian)

Core = Node ("Core")
LIE.insert_left(Core)

ItaloCeltic = Node("Italo-Celtic","I-C")
LIE.insert_right(ItaloCeltic)

GkArmII = Node("Gk–Arm–I-I","GAII")
Core.insert_left(GkArmII)

BaltoSlavic = Node("Balto-Slavic","B-S")
Core.insert_right(BaltoSlavic)

Italic = Node("Italic")
ItaloCeltic.insert_left(Italic)

Celtic = Node("Celtic")
ItaloCeltic.insert_right(Celtic)

GkArm = Node("Gk-Arm","GA")
GkArmII.insert_left(GkArm)

IndoIranian = Node("Indo-Iranian","I-I")
GkArmII.insert_right(IndoIranian)

Baltic = Node("Baltic")
BaltoSlavic.insert_left(Baltic)

Slavic = Node("Slavic")
BaltoSlavic.insert_right(Slavic)

OldWestSlavic = Node("OldWestSlavic")
Slavic.insert_left(OldWestSlavic)

WesternSlavic = Node("WesternSlavic")
Slavic.insert_right(WesternSlavic)

Lechitic = Node("Lechitic")
OldWestSlavic.insert_left(Lechitic)

Polish = Node("Polish")
Lechitic.insert_left(Polish)

OldPolish = Node("OldPolish")
Lechitic.insert_right("OldPolish")

Sorbian = Node("Sorbian")
OldWestSlavic.right(Sorbian)

Slovene = Node("Slovene")
WesternSlavic.insert_left(Slovene)

SerboCroatian = Node("SerboCroatian")
WEsternSlavic.insert_right(SerboCroatian)

Greek = Node("Greek","Gk")
GkArm.insert_left(Greek)

Armenian = Node("Armenian","Arm")
GkArm.insert_right(Armenian)

IndoAryan = Node("Indo-Aryan","I-A")
IndoIranian.insert_left(IndoAryan)

Iranian = Node("Iranian")
IndoIranian.insert_right(Iranian)
