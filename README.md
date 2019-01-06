# Passaporto Checker

A simple tool that notifies you when an appointment for an Italian passport request or renewal is available.

### Usage

To use the tool clone this repository and create a configuration file `config.ini` with the format used in `example.config.ini`

In order for email notifications to work you have to create a Mailgun account. Head to mailgun.com, sign up and create a new domain. Then head to the domain control page and copy the domain name and api key and replace them in your configuration. After this is done you can build the docker image with the following command:

```bash
docker build . -t passaporto-checker
```

After the image is built run a container with the following command

```bash
docker run -d --name passaporto -v $(pwd):/usr/workspace:rw passaporto-checker
```