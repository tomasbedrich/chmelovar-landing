from llconfig import Config
from llconfig.converters import bool_like

c = config = Config()
c.init('SENDGRID_API_KEY', str, None)
c.init('MONGO_CONNECTION_STRING', str)
c.init('CONTACT_FORM_RECEPIENT', str, 'ja@tbedrich.cz')
c.init('CONTACT_FORM_SUBJECT', str, 'Chmelovar.cz - dotaz')
c.init('FORCE_HTTPS', bool_like, False)
c.init('DISABLE_DOCS', bool_like, False)
c.init('SENTRY_DSN', str, None)
c.init('SENTRY_ENVIRONMENT', str, 'production')
c.load()
