from flask import Flask, request, jsonify

app = Flask(__name__)

# Memory buffer to simulate basic AI movement memory
movement_buffer = []

@app.route("/", methods=["GET"])
def root():
    return "✅ Billy Brain is online!"

@app.route("/api/movement", methods=["POST"])
def receive_movement():
    try:
        data = request.json
        if not data:
            return jsonify(success=False, error="No data"), 400

        # Optional: limit buffer size
        movement_buffer.append(data)
        if len(movement_buffer) > 100:
            movement_buffer.pop(0)

        print("✅ Movement received:", data)
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e)), 500

@app.route("/api/movement/latest", methods=["GET"])
def get_latest_movement():
    if not movement_buffer:
        return jsonify(success=False, error="No data yet"), 404
    return jsonify(success=True, data=movement_buffer[-1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
