from app import create_app

# Create the app instance using the factory function
app = create_app()

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)