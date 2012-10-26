import bases

"""Amino Acids are instructions which are carried on strand by ribosome"""

aminoacids = {
    'cut':'s', # cut strand(s)
    'del':'s', # delete base from strand
    'swi':'r', # switch enzyme to other strand
    'mvr':'s', # move one unit to the right
    'mvl':'s', # move one unit to the left
    'cop':'r', # turn one Copy mode
    'off':'l', # turn off Copy mode
    'ina':'s', # insert A to the right of this unit
    'inc':'r', # insert C to the right of this unit
    'ing':'r', # insert G to the right of this unit
    'int':'l', # insert T to the right of this unit
    'rpy':'r', # search for the nearest pyrimidine to the right
    'rpu':'l', # search for the nearest purine to the right
    'lpy':'l', # search for the nearest pyrimidine to the left
    'lpu':'l', # search for the nearest purine to the left
}

class Aminoacid:
    pass