#!/bin/env python3

from enum import Enum 

class NotesEnum(Enum):
    C2=0
    Db2=1
    D2=2
    Eb2=3
    E2=4
    F2=5
    Gb2=6
    G2=7
    Ab2=8
    A2=9
    Bb2=10
    B2=11
    C3=12
    Db3=13
    D3=14
    Eb3=15
    E3=16
    F3=17
    Gb3=18
    G3=19
    Ab3=20
    A3=21
    Bb3=22
    B3=23
    C4=24

class MajorScale():
    scale = [
            NotesEnum.C2, 
            NotesEnum.D2, 
            NotesEnum.E2, 
            NotesEnum.F2, 
            NotesEnum.G2, 
            NotesEnum.A2, 
            NotesEnum.B2, 
            NotesEnum.C3, 
            NotesEnum.D3, 
            NotesEnum.E3, 
            NotesEnum.F3, 
            NotesEnum.G3, 
            NotesEnum.A3, 
            NotesEnum.B3, 
            NotesEnum.C4
            ]

class Moves(Enum):
    SteppedUp = 1
    SteppedDown = -1
    SkippedUp = 2
    SkippedDown = -2
    LeaptUpFourth = 3
    LeaptDownFourth = -3
    LeaptUpFifth = 4
    LeaptDownFifth = -4
    LeaptUpSixth = 5
    LeaptDownSixth = -5
    JustBorn = 6

class Cantus():
    lastMove = Moves.JustBorn
    nextMove = Moves.JustBorn

    Notes = [NotesEnum.C3]

def noteChangeGeneric(cantus, intervalChange):
    cantus.lastMove = intervalChange
    lastNote = cantus.Notes[-1]
    scaleDegree = MajorScale.scale.index(lastNote)
    nextNote = scaleDegree + intervalChange
    cantus.Notes.append(MajorScale.scale[nextNote])

def main():
    cantus = Cantus()    
    noteChangeGeneric(cantus, 1)
    noteChangeGeneric(cantus, 1)
    noteChangeGeneric(cantus, -2)
    noteChangeGeneric(cantus, 1)
    noteChangeGeneric(cantus, -1)
    noteChangeGeneric(cantus, 2)
    for note in cantus.Notes:
        print(note)
    

def stepUp(cantus):
    cantus.lastMove= Moves.SteppedUp
    lastNote = cantus.Notes[-1]
    nextNote = lastNote + 1
    cantus.Notes.append(nextNote)
    print("step up")

def stepDown(cantus):
    cantus.LastMove = Moves.SteppedDown
    lastNote = cantus.Notes[-1]
    nextNote = lastNote - 1
    cantus.Notes.append(nextNote)
    print("step down")

def skipUp(cantus):
    cantus.LastMove = Moves.SkippedUp
    lastNote = cantus.Notes[-1]
    nextNote = lastNote + 2
    cantus.Notes.append(nextNote)
    print("skipped up")

def skipDown(cantus):
    cantus.LastMove = Moves.SkippedDown
    lastNote = cantus.Notes[-1]
    nextNote = lastNote - 2
    cantus.Notes.append(nextNote)
    print("skipped Down")

def leapUpFourth(cantus):
    cantus.LastMove = Moves.LeaptUpFourth
    lastNote = cantus.Notes[-1]
    nextNote = lastNote + 3
    cantus.Notes.append(nextNote)
    print("Leapt up fourth")

def leapDownFourth(cantus):
    cantus.LastMove = Moves.LeaptDownFourth
    lastNote = cantus.Notes[-1]
    nextNote = lastNote - 3
    cantus.Notes.append(nextNote)
    print("Leapt Down fourth")

def leapUpFifth(cantus):
    cantus.LastMove = Moves.LeaptUpFifth
    lastNote = cantus.Notes[-1]
    nextNote = lastNote + 4
    cantus.Notes.append(nextNote)
    print("Leapt up fifth")

def leapDownFifth(cantus):
    cantus.LastMove = Moves.LeaptUpFifth
    lastNote = cantus.Notes[-1]
    nextNote = lastNote - 4
    cantus.Notes.append(nextNote)
    print("Leapt down fifth")

def leapUpSixth(cantus):
    cantus.LastMove = Moves.LeaptUpSixth
    lastNote = cantus.Notes[-1]
    nextNote = lastNote + 5
    cantus.Notes.append(nextNote)
    print("Leapt up sixth")

def leapDownSixth(cantus):
    cantus.LastMove = Moves.LeaptUpSixth
    lastNote = cantus.Notes[-1]
    nextNote = lastNote - 5
    cantus.Notes.append(nextNote)
    print("Leapt down sixth")


if __name__=="__main__":
    main()
