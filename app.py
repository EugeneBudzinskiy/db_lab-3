from flask import Flask
from database import database_init_app
from project import project
from project_add import project_add
from project_edit import project_edit


# Create app
app = Flask(__name__)

# Setup configuration
# app.config.from_object('config.DevelopmentConfig')
app.config.from_object('config.ProductionConfig')

# Setup all dependencies
app.app_context().push()
database_init_app(app)

# Register all blueprints
app.register_blueprint(project)
app.register_blueprint(project_add)
app.register_blueprint(project_edit)


if __name__ == "__main__":
    # Run app
    main().run()
