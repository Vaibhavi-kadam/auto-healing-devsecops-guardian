
from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

system_status = {"status": "Running", "last_healed": "Not yet"}

@app.route('/')
def home():
    return jsonify({
        "project": "Auto-Healing DevSecOps Guardian",
        "status": system_status["status"],
        "author": "Vaibhavi Kadam"
    })

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({
        "service": "Guardian Backend",
        "status": system_status["status"],
        "uptime": "99.9%",
        "time": datetime.now().strftime("%H:%M:%S")
    })

@app.route('/heal')
def heal():
    system_status["status"] = "Running"
    system_status["last_healed"] = datetime.now().strftime("%H:%M:%S")
    return jsonify({
        "message": "Auto-Healing Triggered!",
        "action": "Service Restarted Successfully",
        "new_status": "Running",
        "healed_at": system_status["last_healed"]
    })

@app.route('/security')
def security():
    return jsonify({
        "compliance_score": 92,
        "grade": "A",
        "checks": {
            "AWS_S3_Public_Access": "PASS",
            "AWS_IAM_MFA_Enabled": "PASS",
            "AWS_EC2_Open_Ports": "FAIL - Port 22 Open",
            "Docker_Image_Scan": "PASS"
        },
        "vulnerabilities": [
            {"id": "CVE-2024-1234", "severity": "High", "status": "Open"},
            {"id": "CVE-2024-5678", "severity": "Low", "status": "Fixed"}
        ],
        "report_generated_at": datetime.now().strftime("%H:%M:%S")
    })

@app.route('/simulate-failure')
def fail():
    system_status["status"] = "Down"
    return jsonify({"message": "Failure Simulated!", "new_status": "Down"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)