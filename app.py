from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>OpexPanda Deployment</title>
        <style>
            body { font-family: Arial; background: #f0f4f8; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; }
            h1 { color: #2d3748; }
            p { color: #718096; }
            .badge { background: #48bb78; color: white; padding: 6px 16px; border-radius: 20px; font-size: 14px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🐼 OpexPanda Deployment Project</h1>
            <p>Containerized Flask App using Docker</p>
            <br>
            <span class="badge">Running Successfully</span>
            <br><br>
            <p style="font-size:13px; color:#a0aec0;">Deployed by: Samridhi | DevOps Intern</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)