# RabbitMQ MQTT Example

Example of RabbitMQ MQTT

Shared in the hope it is helpful to somebody

## Running
```shell
make up-core
echo "Wait for a while and make sure everything starts"
make up-publisher-consumer
echo "Ctrl+c to exit when ready"
make logs-publisher-consumer
make stop
```
