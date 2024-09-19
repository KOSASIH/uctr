from flask import Flask, request, jsonify
from uctr import UCTR

app = Flask(__name__)

uctr = UCTR("config/uctr.config.json")

@app.route('/run', methods=['POST'])
def run_uctr():
    uctr.run()
    return jsonify({'status': 'success'})

@app.route('/threat_intel_feeds', methods=['GET'])
def get_threat_intel_feeds():
    return jsonify(uctr.threat_intel_feeds)

@app.route('/vulnerability_scanning', methods=['POST'])
def run_vulnerability_scanning():
    uctr.run_vulnerability_scanning()
    return jsonify({'status': 'success'})

@app.route('/exploit_framework', methods=['POST'])
def run_exploit_framework():
    uctr.run_exploit_framework()
    return jsonify({'status': 'success'})

@app.route('/ai_vulnerability_prediction', methods=['POST'])
def run_ai_vulnerability_prediction():
    uctr.run_ai_vulnerability_prediction()
    return jsonify({'status': 'success'})

@app.route('/reporting_visualization', methods=['GET'])
def get_reporting_visualization():
    return jsonify(uctr.reporting_visualization)

@app.route('/incident_response', methods=['POST'])
def run_incident_response():
    uctr.run_incident_response()
    return jsonify({'status': 'success'})

@app.route('/cloud_deployment', methods=['POST'])
def run_cloud_deployment():
    uctr.run_cloud_deployment()
    return jsonify({'status': 'success'})

@app.route('/devops_integration', methods=['POST'])
def run_devops_integration():
    uctr.run_devops_integration()
    return jsonify({'status': 'success'})

@app.route('/plugin_architecture', methods=['GET'])
def get_plugin_architecture():
    return jsonify(uctr.plugin_architecture)

if __name__ == '__main__':
    app.run(debug=True)
