# -*- coding: utf-8 -*-
"""
Generator for Russian names with two words
"""
# load libs ------------------
from grab import Grab
import random
from pymorphy import get_morph
# ----------------------------

# init vars -----------------
morph = get_morph('dicts')  # Morph object
words = []  # array for words from file
adjs = []  # array for words from site
new_adj = ''  # variable for new adjective
g = Grab()  # Grab object
# ---------------------------

# Main block ----------------------------------------------------------------------------------------------

# Load site with adjectives
g.go('http://dict.ruslang.ru/magn.php?act=list&list=%CF%F0%E8%EB%E0%E3%E0%F2%E5%EB%FC%ED%EE%E5')

# load adjectives into array
vals = g.doc.select('//a[starts-with(@href,"?act=search&magn_lex")]')

# set it adjs uppercase and set it unicode
for item in vals:
    adjs.append(item.text().upper().encode('utf-8'))

# Open files --------------------
f = open('word_rus.txt', 'r')
s = open('complete.txt', 'w')
# ----------------------------------

# Read from files and add it to array after unicode encoding
for line in f:
    words.append(line.rstrip().decode('utf-8'))


# Write into file ---------------------------------------------------------------------------
for i in range(1, 100):

    # Random choice from arrays
    te = random.choice(words).upper()
    adj = random.choice(adjs)

    # Get gender and set adjective to correct form
    z = morph.get_graminfo(te)
    for ite in z:
            new_adj = morph.inflect_ru(unicode(adj, 'utf-8'), ite['info'].split(',')[0])

    # Write it to file
    s.write("{1} {0}\n".format(te.encode('utf-8'), new_adj.encode('utf-8')))
