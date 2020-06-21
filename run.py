from flaskblog import create_app


app = create_app()

# if u dont want to use the export variable...use this following codes
if __name__ == "__main__":
    app.run(debug=True)
