El Passolito
===

El Passolito is the saviour of password generation!

Note: [autoenv](https://github.com/kennethreitz/autoenv) is recommended for managing the environment variables required to run El Passolito.

Configuration
---

Shrubbery expects the following environment variables to be available for configuration:

- `DATABASE_URL`: self explanatory

The following variables are optional and have sensible defaults:

- `DEBUG`: Whether to turn on Django's debug output or not. Defaults to `False`
- `MEDIA_ROOT`: The directory where media should be collected and uploaded to. Defaults to a directory called 'media' in the project root directory.
- `STATIC_ROOT`: Where static files should be collected to. Defaults to `${MEDIA_ROOT}/static`
- `DEVELOP_MODE`: Whether to behave as 'in development' (debug mode enabled etc) or not (ie, production mode). This basically enables various helpers used when developing.
- `EXTRA_APPS`: A list of additional django applications to include. This can be used to add, for example, django-debug-toolbar on your own machine. For example: `EXTRA_APPS='debug_toolbar'`
- `PORT`: If running using Foreman or honcho, then you need to set a port to listen on
- `SECRET_KEY`: The Django secret key to use; this has a default value, but should be set for production environments.
