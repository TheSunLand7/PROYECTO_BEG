import slack
import os
from pathlib import Path
from dotenv import load_dotenv #Carga nuestro archivo env

#El punto es para decir que es el directorio actual
env_path = Path(".") / ".env" #Este es el path de nuestro env para usar en este archivo
load_dotenv(dotenv_path=env_path)

#Es parte del modulo Slack API. Hay muchos de ellos pero se va a usar este
#Es para conectar nuestro token creado
client = slack.WebClient(token=os.environ["SLACK_TOKEN"])

#Para enviar los mensajes en el canal creado y eso es todo por ahora
client.chat_postMessage(channel="#testing", text="Ok buddy")
