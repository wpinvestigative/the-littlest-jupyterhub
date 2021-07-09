# WaPo's Littlest JupyterHub

This is a fork of TLJH that's highly customized for our preferred environment. This is in active development so proceed with caution.

## Quick start

Run the command to download the template to `run.sh` and then edit the file to add admin users or use a different branch. Then run the command

```bash
curl https://raw.githubusercontent.com/wpinvestigative/the-littlest-jupyterhub/development/run.sh.template > run.sh
# Run these commands after editing the file
chmod +x run.sh
./run.sh
```

This will run the TLJH installer with some modifications.

## Installation

- [Tutorial to install TLJH on an already running server you have root access to](https://the-littlest-jupyterhub.readthedocs.io/en/latest/install/custom-server.html).
  You should use this if your cloud provider does not already have a direct tutorial,
  or if you have experience setting up servers.

## Documentation

Our latest documentation is at: https://the-littlest-jupyterhub.readthedocs.io
