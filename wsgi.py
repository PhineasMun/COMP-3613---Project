import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import course, staff, allocations
from App.main import create_app
from App.controllers import create_course, get_staff, create_staff
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)
user_cli = AppGroup('user', help='User object commands') 

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''
@app.cli.command("create_course", help="Creates a course")
def course_create(name,description):
    new_course=create_course(name,description)
    print(f'Course Created ')

@app.cli.command("create_staff", help = "Creates a lecturer,TA or tutor")
def staff_create(name,email,role):
    new_staff=create_staff(name,email,role)
    print(f'Staff Member Created')

@app.cli.command("add_staff", help="Allocates staff members to a course")
def allocate_staff(cid,sid):
    staffall=allocate_staff(cid,sid)
    print(staffall)

@app.cli.command("view_staff")
# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>

# user_cli = AppGroup('user', help='User object commands') 


# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)