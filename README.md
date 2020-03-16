# Fake temperature data generator

This script generates a fake temperatures between 18°C and 24°C every minute and writes it to the InfluxDB database. This can we used when testing locally, only the ip address needs to be changed to localhost for Linux or to the ip address of the docker toolbox machine.
In case the default port (8086) for InfluxDB is changed this will need to be changed accordingly.

## Run the script

```
python script.py
```
