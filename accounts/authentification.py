import requests
import sys
from account.models import ListUser


class PersonaAuthentificationBackend(object):

	def authenticate(self, assertion):
		# Send the assertion to Mozilla's verifier service.

		data = {'assertion': assertion, 'audience': 'localhost'}
		print('sending to mozilla', data, file=sys.stderr)
		resp = requests.post('https://verifier.login.persona.org/verify', data=data)
		print('got', resp.content, file=sys.stderr)

		# Did the verifier response
		if resp.ok:
			# Parse the response
			verification_data = resp.json()

			# Check if the assertion was valid
			if verification_data['status'] == 'okay':
				email = verification_data['email']
				try:
					return self.get_user(email)
				except ListUser.DoesNotExist:
					return ListUser.objects.create(email=email)
