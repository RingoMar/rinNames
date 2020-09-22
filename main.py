import os
import operator
import re
import traceback
import spacy
import enchant


class rinDerived():

    def seed_name(self, rname):
        try:
            wrdType = {"ADJ": "adjective", "ADP": "adposition", "ADV": "adverb", "AUX": "auxiliary verb",
            "CONJ": "coordinating conjunction", "DET": "determiner", "INTJ": "interjection", "NOUN": "noun",
            "NUM": "numeral", "PART": "particle", "PRON": "pronoun", "PROPN": "proper noun",
            "PUNCT": "punctuation", "SCONJ": "subordinating conjunction", "SYM": "symbol",
            "VERB": "verb","X": "other"}
            nlp = spacy.load("en_core_web_sm")
            wordPredict = enchant.Dict("en_US")
            foundWords = []
            derivedWords = []
            suggestWords = []
            finalWords = {}
            tags = []
            name = rname.replace("_", " ")
            # If user has a capitals in name split it up 
            r1 = re.findall(r"([A-z][a-z]+)", name)
            try:
                if r1[1]:
                    for Fragname in r1:
                        suggestWords.append(Fragname)
            except IndexError:
                # User doesn't have capitals now looking for other names in name
                for namer in name:
                    try:
                        if wordPredict.check(derivedWords[-1]) and len(derivedWords[-1]) >= 3:
                            foundWords.append(derivedWords[-1])
                            del derivedWords[:]
                        derivedWords.append(derivedWords[-1] + namer)
                    except IndexError:
                        derivedWords.append(namer)

                for decon in derivedWords:
                    suggestWords.append(wordPredict.suggest(decon))
                for decon in foundWords:
                    suggestWords.append(wordPredict.suggest(decon))


            # Take suggested words and put into percentage cal
            for userWord in suggestWords:
                try:
                    if r1[1]:
                        try:
                            wordper = re.search(userWord, name)
                            types = nlp(wordper[0])
                            divF = 100/(len(wordper[0])+len(name))
                            finalWords[round((len(name) * divF), 2)] = [wordper[0]]
                            for token in types:
                                finalWords[round((len(name) * divF), 2)].append(token.text)
                                finalWords[round((len(name) * divF), 2)].append(token.pos_)
                                finalWords[round((len(name) * divF), 2)].append(token.lemma_)
                                finalWords[round((len(name) * divF), 2)].append(token.tag_)
                                finalWords[round((len(name) * divF), 2)].append(token.dep_)
                                finalWords[round((len(name) * divF), 2)].append(token.shape_)
                                finalWords[round((len(name) * divF), 2)].append(token.is_alpha)
                                finalWords[round((len(name) * divF), 2)].append(token.is_stop)
                        except TypeError:
                            pass
                except:
                    for rWordRE in userWord:
                        wordRE = rWordRE.replace("-", "")
                        rWordRE.replace(" ", "")
                        try:
                            wordper = re.search(wordRE, name)
                            types = nlp(wordper[0])
                            divF = 100/(len(wordper[0])+len(name))
                            finalWords[round((len(name) * divF), 2)] = [wordper[0]]
                            for token in types:
                                finalWords[round((len(name) * divF), 2)].append(token.text)
                                finalWords[round((len(name) * divF), 2)].append(token.pos_)
                                finalWords[round((len(name) * divF), 2)].append(token.lemma_)
                                finalWords[round((len(name) * divF), 2)].append(token.tag_)
                                finalWords[round((len(name) * divF), 2)].append(token.dep_)
                                finalWords[round((len(name) * divF), 2)].append(token.shape_)
                                finalWords[round((len(name) * divF), 2)].append(token.is_alpha)
                                finalWords[round((len(name) * divF), 2)].append(token.is_stop)
                        except TypeError:
                            pass

            sorted_dict = dict(sorted(finalWords.items(), key=operator.itemgetter(0)))
            # print(foundWords, derivedWords, suggestWords, finalWords)
            try:
                if len(finalWords[next(iter(sorted_dict))]) >= 3:
                    if int(next(iter(sorted_dict))) <= 80:
                        nameWeWant = ""
                        weWant = {"noun" : True, "pronoun": True, "adverb": True, "adjective": True}
                        for namesWeHave in finalWords.keys():
                                namesWeHAve = (wrdType[finalWords[namesWeHave][2]])
                                try:
                                    if weWant[namesWeHAve]:
                                        if weWant[namesWeHAve] >= 4:
                                            nameWeWant = finalWords[namesWeHave][1]
                                except KeyError:
                                    pass
                                
                        if nameWeWant:
                            return (f"I would call {rname}: {nameWeWant} {sorted_dict}")
                        else:
                            return (f"I dont have a good name for {rname} with 'want': {rname} {sorted_dict} ")
                    else:
                        return (f"I dont have a good name for {rname}: {rname} {sorted_dict} ")
                else:
                    return (f"I dont have a good name for {rname}: {rname} {sorted_dict} ")
            except Exception as e:
                return (f"I dont have a good name for {rname}: {rname} {sorted_dict} {e}")

        except Exception as er:
            return ">>> Couldn't find a good name, using:" + name, er


d = rinDerived()

print(rinDerived().seed_name("GivingClaw"))
