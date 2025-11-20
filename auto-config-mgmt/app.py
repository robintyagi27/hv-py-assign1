from flask import Flask, jsonify
import configparser
import json
import os

app = Flask(__name__)

CONFIG_FILE = "config.ini"
OUTPUT_JSON = "config_output.json"


def parse_config():
    """Parse config.ini and return a dictionary."""
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError("Configuration file not found!")

    config = configparser.ConfigParser()

    try:
        config.read(CONFIG_FILE)
    except Exception as e:
        raise Exception(f"Error reading config file: {str(e)}")

    parsed_data = {}
    for section in config.sections():
        parsed_data[section] = dict(config.items(section))

    return parsed_data


def save_to_json(data):
    """Save parsed configuration to a JSON file."""
    with open(OUTPUT_JSON, "w") as f:
        json.dump(data, f, indent=4)
    return True


def load_from_json():
    """Load configuration from JSON file."""
    if not os.path.exists(OUTPUT_JSON):
        return None
    with open(OUTPUT_JSON, "r") as f:
        return json.load(f)


@app.route("/config", methods=["GET"])
def get_config():
    """API endpoint to fetch saved config JSON."""
    data = load_from_json()
    if not data:
        return jsonify({"error": "No config data found"}), 404
    return jsonify(data)


if __name__ == "__main__":
    try:
        parsed_data = parse_config()
        save_to_json(parsed_data)
        print("Configuration parsed and stored in config_output.json!")
    except Exception as e:
        print(f"Error: {e}")

    app.run(host="0.0.0.0", port=5000)
