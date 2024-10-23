#!/usr/bin/env python3
"""module for listing documents"""

def list_all(mongo_collection):
    """lists all documents in a collection"""
    return list(mongo_collection.find())
