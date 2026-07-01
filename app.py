from flask import Flask
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info("Home page visited")
    return '''
    <html>
    <head>
        <title>OpexPanda Deployment</title>
        <style>
            body { font-family: Arial; background: #f0f4f8; margin: 0; }
            nav { background: #2d3748; padding: 15px 40px; display: flex; gap: 20px; }
            nav a { color: white; text-decoration: none; font-size: 15px; }
            nav a:hover { color: #48bb78; }
            .container { display: flex; justify-content: center; align-items: center; height: 85vh; }
            .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); text-align: center; }
            h1 { color: #2d3748; }
            p { color: #718096; }
            .badge { background: #48bb78; color: white; padding: 6px 16px; border-radius: 20px; font-size: 14px; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">🏠 Home</a>
            <a href="/about">📄 About</a>
            <a href="/status">📊 Status</a>
            <a href="/health">❤️ Health</a>
        </nav>
        <div class="container">
            <div class="card">
                <h1>🐼 OpexPanda Deployment Project</h1>
                <p>Containerized Flask App using Docker</p>
                <br>
                <span class="badge">Running Successfully</span>
                <br><br>
                <p style="font-size:13px; color:#a0aec0;">Deployed by: Samridhi | DevOps Intern</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/about')
def about():
    logger.info("About page visited")
    return '''
    <html>
    <head>
        <title>About - OpexPanda</title>
        <style>
            body { font-family: Arial; background: #f0f4f8; margin: 0; }
            nav { background: #2d3748; padding: 15px 40px; display: flex; gap: 20px; }
            nav a { color: white; text-decoration: none; font-size: 15px; }
            nav a:hover { color: #48bb78; }
            .container { display: flex; justify-content: center; align-items: center; height: 85vh; }
            .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 500px; }
            h1 { color: #2d3748; }
            li { color: #718096; margin: 10px 0; }
            .tag { background: #ebf8ff; color: #2b6cb0; padding: 4px 12px; border-radius: 20px; font-size: 13px; margin: 4px; display: inline-block; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">🏠 Home</a>
            <a href="/about">📄 About</a>
            <a href="/status">📊 Status</a>
            <a href="/health">❤️ Health</a>
        </nav>
        <div class="container">
            <div class="card">
                <h1>📄 About This Project</h1>
                <p><b>Problem:</b> Manual deployments were error-prone and inconsistent.</p>
                <p><b>Solution:</b> Containerized the app using Docker for consistent deployments.</p>
                <p><b>Tech Stack:</b></p>
                <div>
                    <span class="tag">Python Flask</span>
                    <span class="tag">Docker</span>
                    <span class="tag">Docker Compose</span>
                    <span class="tag">GitHub Actions</span>
                    <span class="tag">Ubuntu</span>
                </div>
                <br>
                <p><b>Intern:</b> Samridhi Singh | DevOps Team | OpexPanda</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/status')
def status():
    logger.info("Status page visited")
    return '''
    <html>
    <head>
        <title>Status - OpexPanda</title>
        <style>
            body { font-family: Arial; background: #f0f4f8; margin: 0; }
            nav { background: #2d3748; padding: 15px 40px; display: flex; gap: 20px; }
            nav a { color: white; text-decoration: none; font-size: 15px; }
            nav a:hover { color: #48bb78; }
            .container { display: flex; justify-content: center; align-items: center; height: 85vh; }
            .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); min-width: 400px; }
            h1 { color: #2d3748; }
            .row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #e2e8f0; }
            .green { color: #48bb78; font-weight: bold; }
            .blue { color: #4299e1; font-weight: bold; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">🏠 Home</a>
            <a href="/about">📄 About</a>
            <a href="/status">📊 Status</a>
            <a href="/health">❤️ Health</a>
        </nav>
        <div class="container">
            <div class="card">
                <h1>📊 Project Status</h1>
                <div class="row"><span>Internship Week</span><span class="blue">Week 4 of 8</span></div>
                <div class="row"><span>Docker Container</span><span class="green">✅ Running</span></div>
                <div class="row"><span>CI/CD Pipeline</span><span class="green">✅ Active</span></div>
                <div class="row"><span>GitHub Repo</span><span class="green">✅ Connected</span></div>
                <div class="row"><span>Next Milestone</span><span class="blue">Nginx Integration</span></div>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    logger.info("Health check endpoint hit")
    return {"status": "healthy", "app": "OpexPanda Deployment", "intern": "Samridhi"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)