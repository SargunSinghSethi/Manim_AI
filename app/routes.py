from flask import Blueprint, jsonify, request
from app.utils.filters import is_prompt_unsafe
from app.utils.openai_client import get_manim_code
from app.utils.ast_sanitizer import sanitize_ast
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Flask backend is working!"})


@main.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    user_prompt = data.get("prompt","")
    print(user_prompt)

    # Step 1: Pre-check for malicious intent
    flagged, reason = is_prompt_unsafe(user_prompt)

    if flagged:
        return jsonify({
            "status": "abort",
            "reason": reason
        }), 400
    

    print(user_prompt)
    # Step 2: Send to OpenAI
    response = get_manim_code(user_prompt)
    print(response)

    if response.get("status") == "rejected":
        return jsonify({"status": "rejected", "reason": response.get("reason")}), 400
    
    code = response.get("code", "")

    # Step 3: AST sanitizer
    safe, reason = sanitize_ast(code)
    if not safe:
        return jsonify({
            "status" : "rejected",
            "reason" : f"AST Sanitizer: {reason}"
        }), 400
    
    
    # Step 4: Return clean code
    return jsonify({
        "status": "accepted",
        "code": code
    }), 200
