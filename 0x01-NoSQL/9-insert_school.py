#!/usr/bin/env python3
"""module for inserting a new document"""

def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document in a collection.
    
    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing the document fields.
        
    Returns:
        The ID of the inserted document.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
