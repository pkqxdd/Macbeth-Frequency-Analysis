from collections import Counter
import sys

import string

f = open("macbeth.txt")
t = f.read()
ft = ''
for c in t:
    if c in string.ascii_letters or c == ' ':
        ft += c.lower()
l = ft.split()

prepositions = ['aboard', 'about', 'above', 'absent', 'across', 'after', 'against', 'along', 'alongside', 'amid',
                'amidst', 'among', 'amongst', 'around', 'as', 'aside', 'astride', 'at', 'athwart', 'atop', 'barring',
                'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'betwixt', 'beyond', 'but',
                'by', 'circa', 'concerning', 'despite', 'down', 'during', 'except', 'excluding', 'failing', 'following',
                'for', 'from', 'given', 'in', 'including', 'inside', 'into', 'like', 'mid', 'minus', 'near', 'next',
                'notwithstanding', 'of', 'off', 'on', 'onto', 'opposite', 'out', 'outside', 'over', 'pace', 'past',
                'per', 'plus', 'pro', 'qua', 'regarding', 'round', 'save', 'since', 'than', 'through', 'thru',
                'throughout', 'thruout', 'till', 'times', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike',
                'until', 'up', 'upon', 'versus', 'via', 'vice', 'with', 'within', 'without']

pronouns = ['all', 'another', 'any', 'anybody', 'anyone', 'anything', 'as', 'both', 'each', 'either', 'everybody',
            'everyone', 'everything', 'few', 'he', 'her', 'hers', 'herself', 'him', 'himself', 'his', 'i', 'it',
            'itself', 'many', 'me', 'mine', 'most', 'my', 'myself', 'neither', 'no', 'one', 'nobody', 'none', 'nothing',
            'one', 'other', 'others', 'our', 'ours', 'ourselves', 'several', 'she', 'some', 'somebody', 'someone',
            'something', 'such', 'that', 'thee', 'their', 'theirs', 'them', 'themselves', 'these', 'they', 'thine',
            'this', 'those', 'thou', 'thy', 'us', 'we', 'what', 'whatever', 'which', 'whichever', 'who', 'whoever',
            'whom', 'whomever', 'whose', 'you', 'your', 'yours', 'yourself', 'yourselves','there']

conjunctions = ['accordingly', 'also', 'anyway', 'besides', 'consequently', 'finally', 'for', 'example', 'for',
                'instance', 'further', 'furthermore', 'hence', 'however', 'incidentally', 'indeed', 'in', 'fact',
                'instead', 'likewise', 'meanwhile', 'moreover', 'namely', 'now', 'of', 'course', 'on', 'the',
                'contrary', 'on', 'the', 'other', 'hand', 'otherwise', 'nevertheless', 'next', 'nonetheless',
                'similarly', 'so', 'far', 'until', 'now', 'still', 'then', 'therefore', 'thus', 'after', 'although',
                'as', 'as', 'if', 'as', 'long', 'as', 'because', 'before', 'even', 'if', 'even', 'though', 'if', 'once',
                'provided', 'since', 'so', 'that', 'that', 'though', 'till', 'unless', 'until', 'what', 'when',
                'whenever', 'wherever', 'whether', 'while', 'and', 'or', 'but', 'nor', 'so', 'for', 'yet']

be = ['be','am','is','are','was','were']

names= ['macbeth','donalbain','ross','duncan','lennox','angus','banquo','fleance','macduff','malcolm']

exclude = ["the", 'an', 'a'] + pronouns + prepositions + conjunctions +be+names



nl = []

for word in l:
    if not word in exclude:
        nl.append(word)



f=open("macbeth_filtered.csv",'w+')

sys.stdout=f

print("Word,Occurrence")
for t in Counter(nl).most_common(100):
    print(t[0]+','+str(t[1]))

f.close()

f=open("macbeth_unfiltered.csv",'w+')

sys.stdout=f

print("Word,Occurrence")
for t in Counter(l).most_common(100):
    print(t[0]+','+str(t[1]))

f.close()