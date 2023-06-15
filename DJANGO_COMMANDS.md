# Django CLI commands

Contents

- [showmigrations](#showmigrations)
- [migrate](#migrate)
- [dbshell](#dbshell)
- [Check all migrations](#check-all-migrations)
- [makemigrations](#makemigrations)
- [Empty fields are disallowed in Django](#empty-fields-are-disallowed-in-django)
- [Check the SQL Command](#check-the-sql-command)
- [migrate](#migrate)
- [createsuperuser](#createsuperuser)

## showmigrations

Each line shows changes to database, initially it will be about creating the data structure.

```bash
python manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
```

## migrate

```bash
python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

## dbshell

Connect to **db.sqlite3** to verify the table contents

```bash
python manage.py dbshell
SQLite version 3.39.5 2022-10-14 20:58:05
Enter ".help" for usage hints.
sqlite>
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
sqlite>
```

.tables will return the list of available tables

## Check all migrations

```bash
sqlite> select * from django_migrations;
1|contenttypes|0001_initial|2023-06-13 12:34:26.030894
2|auth|0001_initial|2023-06-13 12:34:26.048709
3|admin|0001_initial|2023-06-13 12:34:26.061061
4|admin|0002_logentry_remove_auto_add|2023-06-13 12:34:26.089168
5|admin|0003_logentry_add_action_flag_choices|2023-06-13 12:34:26.095675
6|contenttypes|0002_remove_content_type_name|2023-06-13 12:34:26.113741
7|auth|0002_alter_permission_name_max_length|2023-06-13 12:34:26.124719
8|auth|0003_alter_user_email_max_length|2023-06-13 12:34:26.133745
9|auth|0004_alter_user_username_opts|2023-06-13 12:34:26.141336
10|auth|0005_alter_user_last_login_null|2023-06-13 12:34:26.153591
11|auth|0006_require_contenttypes_0002|2023-06-13 12:34:26.155496
12|auth|0007_alter_validators_add_error_messages|2023-06-13 12:34:26.162182
13|auth|0008_alter_user_username_max_length|2023-06-13 12:34:26.173746
14|auth|0009_alter_user_last_name_max_length|2023-06-13 12:34:26.183000
15|auth|0010_alter_group_name_max_length|2023-06-13 12:34:26.193344
16|auth|0011_update_proxy_permissions|2023-06-13 12:34:26.199454
17|auth|0012_alter_user_first_name_max_length|2023-06-13 12:34:26.210032
18|sessions|0001_initial|2023-06-13 12:34:26.214600

```

## makemigrations

After adding a new table to the models, it's important to run the makemigrations command. This will make sure that the table is sync with our local changes.
The app needs to be in the **INSTALLED_APPS** in the **settings.py** if not the migration will not happen. A new file will be created in the **migrations** folder.

```bash
python manage.py makemigrations
Migrations for 'meetings':
  meetings/migrations/0001_initial.py
    - Create model Meeting
```

## Empty fields are disallowed in Django

This happens when columns are added after the table has been populated with values:

```bash
python manage.py makemigrations
It is impossible to add a non-nullable field 'duration' to meeting without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:
```

## Check the SQL Command

To actually see the SQL command that will be generated from the script run the following

```bash
python manage.py sqlmigrate meetings 0001
BEGIN;
--
-- Create model Meeting
--
CREATE TABLE "meetings_meeting" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(250) NOT NULL, "date" date NOT NULL);
COMMIT;
```

## migrate

```bash
python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, meetings, sessions
Running migrations:
  Applying meetings.0001_initial... OK
```

## createsuperuser

Edit data with admin interface

```bash
> python manage.py createsuperuser
Username (leave blank to use 'elisascandellari'): admin
Email address:
Password:
Password (again):
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

# HTML Formatting

## Hardcoded

<a href="/meetings/{{ meeting.id }}">{{ meeting.title }}</a>

## Softcoded

The 'detail' is name given in the urls.py
`<a href="{% url 'detail' meeting.id%}">{{ meeting.title }}</a>`

```code
    path("meetings/<int:id>", detail, name="detail"),
```
