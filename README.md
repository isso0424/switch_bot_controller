#README
##switch bot on python
###Request Modules
- gattlib==0.20200122
- PyBluez==0.23
- pyserial==3.4
###How to use
    import switch_bot
    switch_bot.main(time_out_sec, addr, command)
####arguments
- time_out_sec
    - type = int
    - Number of seconds before timeout
- addr
    - type = str
    - BLE MAC address of switch bot(You can check on switch bot app)
- command
    - type = str
    - Decide switch bot's motion
    - This argument value is only "press", "on" or "off"
