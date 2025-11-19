from app import app, main_agent, sessions
from flask import request
from app.services.chat_agent import sendMessageToAgent

@app.route('/chat', methods=['POST'])
def chat():
    '''
    Envía un mensaje al chatbot
    ---
    tags:
      - Chat
    description: Este endpoint permite enviar un mensaje al chatbot, está entrenado con un agente el cual tiene como objetivo ayudar a los usuarios a escribir correos electrónicos, artículos o incluso novelas. Sugiere oraciones, corrige gramática y estilo, o incluso genera texto completo basado en un tema o idea proporcionada por el usuario. Tambien se puede mantener una conversación con el chatbot enviando el id de la conversación en el parametro session.
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hola, ¿cómo estás?
            session:
              type: string
              nullable: true
              example: "Optional_session_id"
    responses:
      200:
        description: Mensaje enviado correctamente
        schema:
          type: string
    '''
    data = request.get_json(force=True)
    message = data.get('message')
    session = data.get('session')
    try:
        agent = main_agent.agent
        if session:
            session = sessions.get_session(session)
        response = sendMessageToAgent(message, agent, session=session)
        return response
    except Exception as e:
        return str(e)