from flask import Blueprint, request, jsonify
import ast, io, multiprocessing, traceback, queue
from contextlib import redirect_stdout, redirect_stderr

playground_bp = Blueprint("playground", __name__, url_prefix="/playground")

def execute_snippet_worker(code: str, result_queue) -> None:
    output_buffer = io.StringIO()
    error_buffer = io.StringIO()
    try:
        compiled = compile(code, filename="<codelucid-playground>", mode="exec")
        with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
            exec(compiled, {"__builtins__": __builtins__}, {})
        result_queue.put({"ok": True, "output": output_buffer.getvalue() + error_buffer.getvalue()})
    except Exception:
        result_queue.put({"ok": False, "output": output_buffer.getvalue(), "error": traceback.format_exc()})

@playground_bp.route("/run", methods=["POST"])
def run():
    payload = request.get_json(silent=True) or {}
    code = str(payload.get("code", ""))
    
    ctx = multiprocessing.get_context("spawn")
    q = ctx.Queue()
    p = ctx.Process(target=execute_snippet_worker, args=(code, q))
    p.start()
    p.join(4)
    
    if p.is_alive():
        p.terminate()
        return jsonify({"ok": False, "error": "Execution timed out."})
        
    try:
        return jsonify(q.get(timeout=1))
    except queue.Empty:
        return jsonify({"ok": False, "error": "No output returned."})