from fabric.api import env, run


def _get_base_folder(host):
	return '~/sites/' + host


def _get_manage_dot_py(host):
	return '{path}/virtualenv/bin/python {path}/source/manage.py'.format(path=_get_base_folder(host))


def reset_database():

	run('source {}/virtualenv/bin/activate'.format(_get_base_folder(env.host)))
	run('sudo {manage_py} flush'.format(
		manage_py=_get_manage_dot_py(env.host)
	))


def create_session_on_server(email):
	run('source {}/virtualenv/bin/activate'.format(_get_base_folder(env.host)))
	session_key = run('sudo {manage_py} create_session {email}'.format(
		manage_py = _get_manage_dot_py(env.host),
		email=email,
	))
	print(session_key)
