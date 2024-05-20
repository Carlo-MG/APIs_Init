from src import create_app, db

app = create_app()

@app.shell_context_processor
def make():
    return {'db': db}

if __name__ == '__main__':
    app.run()