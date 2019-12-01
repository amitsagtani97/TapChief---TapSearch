import re

class Appearance:
    """
    Contains document's unique ID & the frequency with which a particular work occurs in a document.
    """
    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency

class Database:
    """
    A pseudo database for storing the data.
    """
    def __init__(self):
        self.db = dict()        
    def get(self, id):
        return self.db.get(id, None)
    def add(self, document):
        return self.db.update({document['id']: document['text']})
    def remove(self, document):
        return self.db.pop(document['id'], None)


class InvertedIndex:
    """
    In memory database used to store Inverted Index table
    """
    def __init__(self, db):
        self.index = dict()
        self.db = db
        self.uniqueID = 0

    def index_document(self, documentText, isPdf=False):
        """
        Adds a given document to inverted index table & also updates the database at the same time.

        Arguments:
            documentText -- {str} -- Textual part of a document
            isPDF -- {bool} -- True if a Document submitted is PDF 
        """
        simplifiedTokens = []
        tokens = [token.lower() for token in documentText.split(' ')]
        for token in tokens:
            simplifiedTokens.append(token)
        document = {'id' : self.uniqueID, 'text' : documentText}
        appearances_dict = dict()
        for term in simplifiedTokens:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)
        update_dict = { key: [appearance]
                       if key not in self.index
                       else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items() }
        self.index.update(update_dict)
        self.db.add(document)
        self.uniqueID += 1
        return document
    
    def lookup_query(self, query):
        query = query.lower()
        if query in self.index:
            return (True, {query: self.index[query]})
        else:
            return (False, None)