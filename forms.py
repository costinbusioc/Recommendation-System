from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class RecommendForm(FlaskForm):
    #article_source = StringField('Sursa',
     #       validators=[DataRequired()], widget=TextArea(),
      #      render_kw={"rows": 1, "cols": 16})

    article_title = StringField('Titlu:',
            validators=[DataRequired()], widget=TextArea(),
            render_kw={"rows": 2, "cols": 64})

    #article_content = StringField('Continut', validators=[DataRequired()], widget=TextArea(), render_kw={"rows": 8, "cols": 64})

    #add = SubmitField('Adauga articol')
    recommend = SubmitField('Recomanda articol')
    
    recommended_1 = TextField("Recomandare 1:",
            widget=TextArea(), render_kw={"rows": 2, "cols": 64})
    recommended_2 = TextField("Recomandare 2:",
            widget=TextArea(), render_kw={"rows": 2, "cols": 64})
    
    
    more_recommended_1 = TextField("Similar:",
            widget=TextArea(), render_kw={"rows": 2, "cols": 64})
    more_recommended_2 = TextField("Similar:",
            widget=TextArea(), render_kw={"rows": 2, "cols": 64})
    
    #recommended_source = TextField("Sursa",
     #       widget=TextArea(), render_kw={"rows": 1, "cols": 64})
    #recommended_title = TextField("Titlul",
     #       widget=TextArea(), render_kw={"rows": 2, "cols": 64})
    #recommended_content = TextField("Continut",
     #       widget=TextArea(), render_kw={"rows": 8, "cols": 64})


