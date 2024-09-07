down:
	pkill gunicorn

up:
	gunicorn -w 3 medibot.wsgi:app --daemon

