from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SellForm(FlaskForm):
    product_name = StringField("Produkt", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    amount = StringField("Amount", validators=[DataRequired()])
    submit = SubmitField("Wyslij")