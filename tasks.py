from invoke import task

@task
def start(ctx):
	ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
	ctx.run("APP_ENV=test pytest src", pty=True)

@task
def coverage(ctx):
	ctx.run("APP_ENV=test coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
	ctx.run("APP_ENV=test coverage html", pty=True)

@task
def lint(ctx):
	ctx.run("pylint src", pty=True)

@task
def db_init(ctx):
	ctx.run("mkdir data -p", pty=True)
	ctx.run("python3 src/initialize_database.py", pty=True)
