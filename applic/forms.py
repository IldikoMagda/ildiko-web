from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import InputRequired, Email
 
class ContactForm(FlaskForm):
  name = StringField("Name", [InputRequired("How can I call you?")])
  email = StringField("Email", [InputRequired("Please share your e-mail address with me, won't tell anyone"), Email("Please fill in your e-mail address")])
  subject = StringField("Subject",[InputRequired("What's the topic today?")])
  message = TextAreaField("Message", [InputRequired("Don't be shy, let's talk")])
  submit = SubmitField("Send")