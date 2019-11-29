from llconfig import Config

c = config = Config()
c.init('SENDGRID_API_KEY', str, None)
c.init('MONGO_CONNECTION_STRING', str)
c.init('CONTACT_FORM_RECEPIENT', str, 'ja@tbedrich.cz')
c.init('CONTACT_FORM_SUBJECT', str, 'Chmelovar.cz - dotaz')
c.load()
