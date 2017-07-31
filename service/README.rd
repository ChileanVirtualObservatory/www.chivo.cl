# Service for chivosite

```{r, engine='bash', count_lines}
# Create the file
$ sudo touch /etc/init.d/chivosite
$ sudo chmod +x /etc/init.d/chivosite

# Start chivosite
$ sudo service chivosite start

# Stop chivosite
$ sudo service chivosite stop

# Start chivosite on boot
$ sudo update-rc.d chivosite defaults
```
