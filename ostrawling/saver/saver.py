"""
Authors: Jacob Rawling & Kiran Ostrolenk

@Brief: General class to save generated events to various output files as specified
by the user. 
"""

class Saver:
    def __init__(self):
        pass

def create_saver(saver='csv'):
    if saver == 'csv':
        return Saver()

    return Saver()