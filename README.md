# MQTT connection Rasp to ESP

## Requirements for Raspberry

- [Install mosquitto broker](https://mosquitto.org/download/)

-  Install paho-mqtt 
```console
pip install paho-mqtt
```

- Install Uncomplicated Firewall for easy use
```console
sudo apt install ufw -y
```

- Open port 1883
```code
sudo ufw allow 1883/tcp
```

- Configure mosquitto config file
```console
sudo nano /etc/mosquitto/mosquitto.config
```
- Add at the end of the file the next two lines
```console
listener 1883
allow_anonymous true
```

- Restart mosquitto
```console
sudo systemctl restart mosquitto
```


- Set the system to start automatic mosquitto broker 
```console
sudo systemctl enable mosquitto
sudo ufw reload
sudo reboot
```