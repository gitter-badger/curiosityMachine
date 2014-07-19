from django.db import models
from .templates import EmailTemplate


class Welcome(object):

	@staticmethod
	def mentor(mentor):
		return Welcome().email_mentor(mentor)

	@staticmethod
	def student(student):
		return Welcome().email_student(student)

	@staticmethod
	def underage_student(student):
		return Welcome().email_underage_student(student)

	def email_mentor(self, mentor):
		email = EmailTemplate(['devpopol@gmail.com'], 'welcome_mentor_sbj', 'welcome_mentor', {'mentor': mentor})
		return email.deliver()

	def email_student(self, student):
		email = EmailTemplate(['devpopol@gmail.com'], 'welcome_student_sbj', 'welcome_student', {'student': student})
		return email.deliver()

	def email_underage_student(self, student):
		email = EmailTemplate(['devpopol@gmail.com'], 'welcome_underage_student_sbj', 'welcome_underage_student', {'student': student})
		return email.deliver()
