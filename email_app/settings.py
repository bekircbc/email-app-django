INSTALLED_APPS = [
    # Diğer uygulamalar
    'email_app',
]

# SMTP Ayarları
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025  # MailHog SMTP port
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
