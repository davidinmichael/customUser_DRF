# Custom User Model and Manager

This repository contains the implementation of a custom user model and manager for your Django project. The custom user model allows you to create users with additional fields and customize the authentication process.

## Getting Started

To use the custom user model and manager in your Django project, follow the steps below:

1. Clone this repository to your local machine.

2. Copy the `CustomUser` model and `CustomUserManager` from `models.py` into your Django project.

3. Update your project's settings to use the custom user model:

```python
AUTH_USER_MODEL = 'your_app.CustomUser'
```

4. Migrate your database to create the custom user model table:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Your custom user model is now ready to be used in your project. You can create and authenticate users as you would with the default Django user model.

## Note

Remember to update the `USERNAME_FIELD` and `REQUIRED_FIELDS` attributes in the `CustomUser` model to suit your specific requirements.

## Custom User Fields

The custom user model comes with additional fields that you can use to store more information about your users. The fields are:

- `stack`: A field to store the user's stack (e.g., frontend, backend, full-stack).

- `mobile_number`: A field to store the user's mobile number.

- `address`: A field to store the user's address.

## Custom User Manager

The custom user manager provides methods to create both regular users and superusers. It also includes a method to set a user's password to an unusable value.

## Creating a Superuser

To create a superuser, use the `create_superuser` method provided by the custom user manager. For example:

```python
CustomUser.objects.create_superuser(stack='full-stack', password='mypassword', username='admin')
```

That's it! You now have a custom user model and manager ready to use in your Django project. Happy coding!