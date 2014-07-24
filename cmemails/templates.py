from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template import Context, TemplateDoesNotExist
import os.path

CM_EMAILS_ROOT = os.path.abspath(os.path.dirname(__file__))

templates_path = '../templates'
template_extensions = ('html', 'txt')

class EmailTemplate(object):
	def __init__(self, recipients, subject, template_name, context={}, sender=settings.DEFAULT_FROM_EMAIL):
		self.context = Context(context, autoescape=False)
		self.sender = sender
		self.subject = subject
		self.template_name = template_name
		self.recipients = recipients

	def render_body(self, type='txt'):
		try:
			return render_to_string("%s/%s.%s" % (templates_path, self.template_name, type), self.context)
		except Exception as e:
			print(str(e))
			return None

	def render_subject(self):
		return self.subject

	def render_recipients(self):
		return self.recipients

	#NB: Some things missing here like connection management.
	def deliver(self):
		print(self.render_subject())
		print(self.render_body())
		print(self.sender)
		print(self.render_body('html'))
		
		return send_mail(
			self.render_subject(), 
			self.render_body(), 
			self.sender, 
			self.render_recipients(), 
			html_message=self.render_body('html'), 
			fail_silently=False
		)