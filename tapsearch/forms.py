from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField

class QueryForm(FlaskForm):
    query = StringField('Query', render_kw={"placeholder":"Your Queries Here!"})
    submit = SubmitField('Go!')


class NewDocForm(FlaskForm):
    document = TextAreaField('New Document', render_kw={"placeholder":"Enter new data here"})
    submit = SubmitField('Add')
