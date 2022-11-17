from flask import Flask

def create_app():
    app = Flask(__name__)
    from apps.repository_list.views import repository_list_bp
    from apps.dashboard.views import dashboard_bp
    from apps.login.views import login_bp
    
    app.register_blueprint(repository_list_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(login_bp)
    return app