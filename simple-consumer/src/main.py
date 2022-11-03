from os import getenv
import logging

import time

from dotenv import load_dotenv
from os.path import realpath, dirname
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    logger.info("message received %s", str(message.payload.decode("utf-8")))
    logger.info("message topic=%s", str(message.topic))
    logger.info("message qos=%s", str(message.qos))
    logger.info("message retain flag=%s", str(message.retain))


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    root_dir = realpath(dirname(realpath(__file__)) + "/..")
    load_dotenv(dotenv_path=f"{root_dir}/.env")
    logging.basicConfig(level=getenv("LOGLEVEL", "INFO").upper())

    logger.info("")

    env_configs = {("MQTT_HOST", "rabbitmq", True), ("MQTT_TOPIC", "detections", True), ("MQTT_ID", "consumer", True), }
    config = {}
    for key, default, log in env_configs:
        config[key] = getenv(key, default)
        if log:
            logger.info("%s='%s'", key, str(config[key]))

    client = mqtt.Client(config["MQTT_ID"])
    client.on_message = on_message
    client.connect(config["MQTT_HOST"])
    client.loop_start()
    client.subscribe(config["MQTT_TOPIC"])

    while True:
        try:
            time.sleep(1)
            print(".", end="")
        except KeyboardInterrupt:
            break
    client.loop_stop()
