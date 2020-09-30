import os
import operator
import re
import spacy
os.system("python -m spacy download en_core_web_sm")
import enchant

class rinDerived():

    def seed_name(self, rname):
        try:
            wrdType = {"ADJ": "adjective", "ADP": "adposition", "ADV": "adverb", "AUX": "auxiliary verb",
            "CONJ": "coordinating conjunction", "DET": "determiner", "INTJ": "interjection", "NOUN": "noun",
            "NUM": "numeral", "PART": "particle", "PRON": "pronoun", "PROPN": "propernoun",
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
            nameWeWant = ""

            revName = name[::-1]
            token1 = []
            token2 = []
            for t1 in name:
                try:
                    token1.append(token1[-1] + t1)
                except IndexError:
                    token1.append(t1)

            for t2 in revName:
                try:
                    token2.append(token2[-1] + t2)
                except IndexError:
                    token2.append(t2)
            
            for rev in token2:
                token1.append(rev[::-1])

            # If user has a capitals in name split it up 
            r1 = re.findall(r"([A-z][a-z]+)", name)
            try:
                if r1[1]:
                    for Fragname in r1:
                        suggestWords.append(Fragname)
            except IndexError:
                # User doesn't have capitals now looking for other names in name
                for namer in token1:
                    try:
                        if wordPredict.check(derivedWords[-1]) and len(derivedWords[-1]) >= 3:
                            foundWords.append(derivedWords[-1])
                            del derivedWords[:]
                        derivedWords.append(namer)
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
            print(sorted_dict)
            try:
                if len(finalWords[next(iter(sorted_dict))]) >= 3:
                    vaVl = int(next(iter(sorted_dict))) 
                    if vaVl <= 76:
                        weWant = {"noun" : True, "pronoun": True, "adverb": True, "adjective": True, "propernoun": True}
                        for namesWeHave in sorted_dict.keys():
                            namesWeHAvep2 = (wrdType[finalWords[namesWeHave][2]])
                            try:
                                if weWant[namesWeHAvep2] and nameWeWant == "" and len(finalWords[namesWeHave][1]) >= 3 and namesWeHAvep2 != "bycake":
                                    nameWeWant = finalWords[namesWeHave][1]
                            except KeyError:
                                pass
                                
                        if nameWeWant and len(nameWeWant) >= 4:
                            return [nameWeWant, sorted_dict]
                        else:
                            return [rname, sorted_dict]
                    else:
                        return [rname, sorted_dict]
                else:
                    return [rname, sorted_dict]
            except:
                return [rname, sorted_dict]

        except Exception as e:
            return rname
