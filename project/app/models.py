from mongoengine import Document, fields
import datetime


class UNDocument(Document):
    id = fields.StringField(required=True, primary_key=True)
    title = fields.StringField(required=True)
    document_symbol = fields.StringField(required=True)
    agenda = fields.StringField(required=False, null=True)
    author = fields.StringField(required=False, null=True)
    authority_authors = fields.ListField(required=False, null=True)
    imprint = fields.StringField(required=False, null=True)
    notes = fields.ListField(required=False, null=True)
    publisher = fields.StringField(required=False, null=True)
    pubyear = fields.StringField(required=False, null=True)
    pubdate = fields.StringField(required=False, null=True)
    related_documents = fields.ListField(required=False, null=True)
    subjects = fields.ListField(required=False, null=True)
    summary = fields.StringField(required=False, null=True)
    title_statement = fields.StringField(required=False, null=True)
    links_to_pdf = fields.ListField(required=False, null=True)
    date_modified = fields.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "<UNDocument: document_symbol: {} title: {}".format(
            self.document_symbol.
            self.title
        )


class Blog(Document):
    title = fields.StringField(required=True)
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    body = fields.StringField(required=False, null=True)
    tags = fields.ListField(required=False, null=True)
    is_published = fields.BooleanField(required=False, null=True)

    def __str__(self):
        return self.title
