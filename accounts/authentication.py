import requests
from django.contrib.auth import get_user_model
from superlists.settings import DOMAIN
import logging
User = get_user_model()


PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'


class PersonaAuthenticationBackend(object):

	def authenticate(self, assertion):
		logging.warning('entering authenticate function')
		# Send the assertion to Mozilla's verifier service.
		response = requests.post(
			PERSONA_VERIFY_URL,
			data={'assertion': assertion, 'audience': DOMAIN}
		)
		logging.warning('got response from persona')
		logging.warning(response.content.decode())

		if response.ok and response.json()['status'] == 'okay':
			email = response.json()['email']
			try:
				return User.objects.get(email=email)
			except:
				return User.objects.create(email=email)

	def get_user(self, email):
		try:
			return User.objects.get(email=email)
		except User.DoesNotExist:
			return None
