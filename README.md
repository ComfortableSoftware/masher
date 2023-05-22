
# STANDARD DISCLAIMERS
- My coding style has made it mostly unmodified through every language I have coded in since around 1977.
  - It's opinionated, possibly over/under-readable depending on your personal style.

# INFORMATION
- This app installs itself globally with configuration copied to '~/.config/masher/*'
  - There are utilities in 'masher.CONF_D' to manage building configuration files.
    - These are currently primitive and will improve over time.
  - After install '<CONFIG_DIR>/CONF_D' has example profiles and actions to perform modules.
- No stubs are installed.
  - All access to the module is done through 'python -m masher.module'
- The module 'masher.server' is a daemon that listens on port 29016 for mouse, gamepad, and keyboard events to send to the system as if you executed them on the appropriate devices.
  - This requires root access when it's installed (recommended method), or root access every time it's executed which leaves you wide open to miscreants taking over your system easily.
  - ***Because 'masher.server' needs to run as root it is unwise to install this package editable and/or in userspace‼‼***
    - All a miscreant needs to do is edit the server.py file and reboot, as soon as that file executes their code runs as root.
- The module 'masher.client'
