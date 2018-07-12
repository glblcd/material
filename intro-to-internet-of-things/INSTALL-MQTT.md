## Installing Mosquitto MQTT client on Rapsberry Pi

```
sudo -s # Be careful - the rest of these commands are run as root / administrator
wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
sudo apt-key add mosquitto-repo.gpg.key 
cd /etc/apt/sources.list.d/
wget http://repo.mosquitto.org/debian/mosquitto-stretch.list
apt-get update
apt-get install mosquitto-clients
^D # Ctrl-D - this exits the root / administrator shell - always do this when finished
```

### Beginners Guide To The MQTT Protocol

http://www.steves-internet-guide.com/mqtt/

Using the `Mosquitto_pub` and `Mosquitto_sub` MQTT Client Tools

Examples

http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/

E.g.

In One window / tab:

```
mosquitto_sub -h 82.165.16.151 -t UCC/mark
```

In another window / tab:

```
mosquitto_pub -h 82.165.16.151 -m "Hi" -t UCC/mark
```

### Using Paho in python with MQTT

http://www.steves-internet-guide.com/into-mqtt-python-client/

