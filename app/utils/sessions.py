from agents import SQLiteSession


class Sessions:
    def __init__(self):
        self.sessions = {}

    def get_session(self, session_id: str):
        """
        Devuelve la sesión si existe, o la crea y la guarda en memoria.
        """
        if not session_id:
            return None

        if session_id not in self.sessions:
            self.sessions[session_id] = SQLiteSession(session_id)
        return self.sessions[session_id]

    def create_session(self, session_id: str):
        """
        Crea explícitamente una sesión (o devuelve la existente).
        """
        return self.get_session(session_id)

    def delete_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

    def delete_all_sessions(self):
        self.sessions = {}