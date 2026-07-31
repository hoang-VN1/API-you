import os
import requests
from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# === CẤU HÌNH ===
PLACE_ID = os.getenv("PLACE_ID", "4442272183")  # Blox Fruits
API_KEY = os.getenv("API_KEY", "HOANG_kunBEZRBTa")

# === XÁC THỰC ===
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.args.get('api_key')
        if not key or key != API_KEY:
            return jsonify({"error": "Invalid or missing API key"}), 401
        return f(*args, **kwargs)
    return decorated

# === LẤY DANH SÁCH SERVER (CHỈ LẤY SERVER CÒN CHỖ) ===
def fetch_servers():
    """
    Gọi Roblox API và chỉ trả về các server còn chỗ trống.
    """
    url = f"https://games.roblox.com/v1/games/{PLACE_ID}/servers/Public?limit=100&excludeFullGames=true&sortOrder=Desc"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        # Lọc thêm một lần nữa để chắc chắn (phòng trường hợp Roblox API không lọc đúng)
        servers = data.get('data', [])
        filtered = [s for s in servers if s.get('playing', 0) < s.get('maxPlayers', 0)]
        return filtered
    except Exception as e:
        print(f"[ERROR] Không lấy được server: {e}")
        return []

# === DANH SÁCH BOSS HỖ TRỢ ===
BOSS_LIST = [
    'full_moon', 'dough_king', 'rip_indra', 'darkbeard',
    'soul_reaper', 'cursed_captain', 'mirage', 'kitsune',
    'leviathan', 'frozen_dimension', 'prehistoric',
    'sword_dealer', 'haki_dealer', 'pirate_raid',
    'cake_prince', 'cake_queen', 'tyrant', 'elite',
    'fruit', 'berry', 'cake_spawner'
]

# === ROUTE CHÍNH ===
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Blox Hop API",
        "endpoints": "/boss/<name>?api_key=YOUR_KEY",
        "note": "Chỉ trả về server còn chỗ trống"
    })

# === ROUTE ĐỘNG CHO TẤT CẢ BOSS ===
@app.route('/boss/<boss_name>')
@require_api_key
def get_boss_servers(boss_name):
    if boss_name not in BOSS_LIST:
        return jsonify({"error": f"Boss '{boss_name}' không tồn tại"}), 404
    servers = fetch_servers()
    return jsonify({
        "success": True,
        "boss": boss_name,
        "total": len(servers),
        "data": servers
    })

# === XỬ LÝ LỖI ===
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# === CHẠY SERVER ===
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)    'soul_reaper', 'cursed_captain', 'mirage', 'kitsune',
    'leviathan', 'frozen_dimension', 'prehistoric',
    'sword_dealer', 'haki_dealer', 'pirate_raid',
    'cake_prince', 'cake_queen', 'tyrant', 'elite',
    'fruit', 'berry', 'cake_spawner'
]

# === ROUTE CHÍNH ===
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Blox Hop API",
        "endpoints": "/boss/<name>?api_key=YOUR_KEY"
    })

# === ROUTE ĐỘNG CHO TẤT CẢ BOSS ===
@app.route('/boss/<boss_name>')
@require_api_key
def get_boss_servers(boss_name):
    if boss_name not in BOSS_LIST:
        return jsonify({"error": f"Boss '{boss_name}' không tồn tại"}), 404
    servers = fetch_servers()
    return jsonify({
        "success": True,
        "boss": boss_name,
        "data": servers
    })

# === XỬ LÝ LỖI ===
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# === CHẠY SERVER ===
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)        print(f"[ERROR] Không lấy được server: {e}")
        return []

# === DANH SÁCH BOSS HỖ TRỢ ===
BOSS_LIST = [
    'full_moon', 'dough_king', 'rip_indra', 'darkbeard',
    'soul_reaper', 'cursed_captain', 'mirage', 'kitsune',
    'leviathan', 'frozen_dimension', 'prehistoric',
    'sword_dealer', 'haki_dealer', 'pirate_raid',
    'cake_prince', 'cake_queen', 'tyrant', 'elite',
    'fruit', 'berry', 'cake_spawner'
]

# === ROUTE CHÍNH ===
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Blox Hop API",
        "endpoints": "/boss/<name>?api_key=YOUR_KEY",
        "note": "Chỉ trả về server còn chỗ trống"
    })

# === ROUTE ĐỘNG CHO TẤT CẢ BOSS ===
@app.route('/boss/<boss_name>')
@require_api_key
def get_boss_servers(boss_name):
    if boss_name not in BOSS_LIST:
        return jsonify({"error": f"Boss '{boss_name}' không tồn tại"}), 404
    servers = fetch_servers()
    return jsonify({
        "success": True,
        "boss": boss_name,
        "total": len(servers),
        "data": servers
    })

# === XỬ LÝ LỖI ===
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# === CHẠY SERVER ===
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)    'soul_reaper', 'cursed_captain', 'mirage', 'kitsune',
    'leviathan', 'frozen_dimension', 'prehistoric',
    'sword_dealer', 'haki_dealer', 'pirate_raid',
    'cake_prince', 'cake_queen', 'tyrant', 'elite',
    'fruit', 'berry', 'cake_spawner'
]

# === ROUTE CHÍNH ===
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "service": "Blox Hop API",
        "endpoints": "/boss/<name>?api_key=YOUR_KEY"
    })

# === ROUTE ĐỘNG CHO TẤT CẢ BOSS ===
@app.route('/boss/<boss_name>')
@require_api_key
def get_boss_servers(boss_name):
    if boss_name not in BOSS_LIST:
        return jsonify({"error": f"Boss '{boss_name}' không tồn tại"}), 404
    servers = fetch_servers()
    return jsonify({
        "success": True,
        "boss": boss_name,
        "data": servers
    })

# === XỬ LÝ LỖI ===
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# === CHẠY SERVER ===
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
