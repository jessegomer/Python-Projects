#
#Made by Jesse Gomer
#Requires NLTK (Natural Language Tool Kit)
#It runs but the output is very unnatural
'''
This takes an input file and a file to convert, and it tries to convert the style
of the file to convert to the style of the other.
Essentially it tries to replace words and replace them with ones that are more common
in the other file.
'''

import re
import random
import sys
try:
        import nltk
        from nltk.corpus import wordnet as wn
except:
         sys.exit("Sorry you need the NLTK module to run this program")
        
        
class MimicMaker( object ):
        def __init__(self):
                self.fd = {}
                self.exceptedWords = ["a","the","an", "", "i", "me"]

                
        #adds the words in a file to the frequency
        def addFileToFreq(self, filename):
                word_list = re.split('\s+', file(filename).read().lower())
                punc = re.compile(r'[.?!,":;]')
                for word in word_list:
                        word  = punc.sub("", word)
                        try: 
                                self.fd[word] += 1
                        except:
                                self.fd[word] = 1
                
        #takes the list of possibilites and normalizes it to 100
        def getProbabilities(self, possibilitiesList, originalWord):
                total = 0
                goodWords = []
                probs = []
                cutoffs = 0
                for word in possibilitiesList:
                        try:
                                total += self.fd[word]
                                goodWords += [word]
                        except:
                                continue
                if len(goodWords) == 0:
                        return [originalWord, 100]
                
                for word in goodWords:
                        probs += [[word, self.fd[word]/(total*1.0)*100]]
                        
                return probs
        
        #takes the word/probability list and chooses a word from it
        def chooseWord(self, probs):
                rand = random.randint(0,100)
                total = 0
                try:
                        for word, chance in probs:
                                total += chance
                                if rand < total :
                                        return word
                except:
                        return ""

        def convertFile(self, fromFile, toFile):
                ff = open(fromFile)
                tf = open(toFile, "w")
                punc = re.compile(r'[.?!,":;\n]')
                num = re.compile(r'(0-9)')

                for line in ff:
                        removed = punc.sub("",line)
                        words = re.split(r'\s+',removed)
                        for word in words:
                                if word in self.exceptedWords:
                                        continue
                                if (num.search(word) is None):
                                        try:
                                                syn = self.getSyn(word)
                                                probs = self.getProbabilities(syn, word)
                                                chosen = self.chooseWord(probs)
                                                line = re.sub(word, chosen, line, 1)
                                        except:
                                                continue
                        print >>tf, line

                tf.close()
                ff.close()
                                         

        def getSyn(self, word):
                syns = []
                try:
                        for one in wn.synsets(word):
                            for l in one.lemmas:
                                syns.append(l.name)

                        syns = list(set(syns))
                        return syns
                except:
                        return [word]



                

m  = MimicMaker()
inFileName = raw_input("What is the file name of the input file? ")
toConvertFile = raw_input("What is the file of the name you want stylized? ")
outFileName = raw_input("What is the outfile name? ")
m.addFileToFreq(inFileName)
m.convertFile(toConvertFile, outFileName)

