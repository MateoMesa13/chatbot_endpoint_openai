# Chatbot Endpoint con OpenAI Agents SDK

API en Flask que expone un endpoint de chat basado en el **OpenAI Agents SDK** (`openai-agents`), documentado con **Flasgger / Swagger** y con soporte para **sesiones de conversación** mientras el servidor esté activo.

---

## Estructura del proyecto

```text
chatbot_endpoint_openai/
│
├── app/
│   ├── __init__.py           # Crea la app Flask, inicializa Swagger, MainAgent y Sessions
│   │                         # Expone: app, main_agent, sessions
│   ├── agents/
│   │   └── main_agent.py     # Configuración del agente (modelo, instrucciones/prompt)
│   ├── routes/
│   │   ├── chat.py           # Endpoint /chat (POST) para hablar con el agente
│   │   └── health.py         # Endpoint /health (GET) para comprobar el estado
│   ├── services/
│   │   └── chat_agent.py     # Lógica para llamar a Runner.run_sync (OpenAI Agents SDK)
│   └── utils/
│       └── sessions.py       # Gestor en memoria de sesiones (Sessions -> SQLiteSession)
│
├── main.py                   # Punto de entrada: arranca la app Flask
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Este archivo

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
    git clone {Repository}
    cd chatbot_endpoint_openai
    pip install -r requirements.txt
    python main.py
```

## Documentación

La documentación se encuentra en la ruta `/apidocs/`.

## Ejemplo de uso

```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "Hola, ¿cómo estás?"}'
```

## Sesiones

Se pueden mantener sesiones de conversación enviando el id de la conversación en el parametro session.

```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "Hola, ¿cómo estás?", "session": "123"}'
```