'''
cli_commands list:

@app.cli.command("create_course", help="Creates a course")
def course_create(name,description):
 

@app.cli.command("create_staff", help = "Creates a lecturer,TA or tutor")
def staff_create(name,email,role):


@app.cli.command("add_staff", help="Allocates staff members to a course")
def allocate_staff(cid,sid):


@app.cli.command("view_staff", help="views all staff members in a course")
def view_staff(cid):


'''