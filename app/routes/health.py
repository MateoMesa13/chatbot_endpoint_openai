from flask import jsonify
from app import app


@app.route("/health", methods=["GET"])
def health_check():
    """
    Comprobar estado de la API
    ---
    tags:
      - Misc
    responses:
      200:
        description: La API está funcionando correctamente
        schema:
          type: object
          properties:
            status:
              type: string
              example: ok
    """
    return jsonify({"status": "ok"}), 200