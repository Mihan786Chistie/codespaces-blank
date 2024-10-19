from flask import Flask, render_template_string
import subprocess
import getpass
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the full name (replace with your actual name)
    name = "Syed Md Mihan Chistie"
    
    # Get the system username
    username = getpass.getuser()
    
    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Run top instead of htop (as htop might not be available in all environments)
    try:
        top_output = subprocess.check_output(['top', '-bn1'], text=True)
    except subprocess.CalledProcessError:
        top_output = "Error: Unable to run top command."
    
    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>System Information</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
            h1 { color: #333; }
            pre { background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {{ name }}</p>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Server Time (IST):</strong> {{ server_time }}</p>
        <h2>Top Output:</h2>
        <pre>{{ top_output }}</pre>
    </body>
    </html>
    """
    
    return render_template_string(html_template, name=name, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)