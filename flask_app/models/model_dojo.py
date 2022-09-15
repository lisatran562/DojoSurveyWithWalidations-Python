from flask_app import DB
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def result(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC;"
        results = connectToMySQL(DB).query_db(query)
        return Dojo(results[0])

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name']) < 3:
            is_valid = False
            flash('Name must be at least 3 characters', 'err_dojo_name')

        if len(data['location']) < 1:
            is_valid = False
            flash('Must choose a location', 'err_dojo_location')

        if len(data['language']) < 1:
            is_valid = False
            flash('Must choose a favorite language', 'err_dojo_language')

        if len(data['comment']) < 3:
            is_valid = False
            flash('Comments must be at least 3 characters', 'err_dojo_comment')

        return is_valid