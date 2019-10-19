from flask import Flask, Blueprint, render_template, request, flash
from applic.forms import ContactForm
from flask_mail import Message, Mail

__author__ = 'Ildiko'


contact_blueprint = Blueprint('contact', __name__)
mail = Mail()

@contact_blueprint.route('/', methods=['GET', 'POST'])
def index(): 
    form= ContactForm()

    if request.method =='POST':
       if form.validate_on_submit()== False:
          return render_template('contact/index.html', form=form)
       else:
            msg = Message(form.subject.data, sender='ildikomagda.web@gmail.com', recipients=['ildiko.magda@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact/index.html', success=True)

    elif request.method =='GET':
        return render_template('contact/index.html', form=form)

