from agents import Runner


def sendMessageToAgent(message, agent, session = None):
    try:
        response = Runner.run_sync(agent, message, session=session)
        return response.final_output
    except Exception as e:
        return str(e)
