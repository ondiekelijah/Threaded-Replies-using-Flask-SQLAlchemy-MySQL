def deploy():
	"""Run deployment tasks."""
	from app import create_app,db

	app = create_app()
	app.app_context().push()

	from models import Post,Comment

	from flask_migrate import upgrade,migrate,init,stamp
	db.create_all()
	
	# migrate database to latest revision
	stamp()
	migrate()
	upgrade()
	
deploy()
	