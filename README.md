# Passaporto Checker

A simple tool that notifies you when an appointment for an Italian passport request or renewal is available on `passaportonline.poliziadistato.it`

### Usage

To use the tool follow these steps:

- Clone this repository
- Create a configuration file `config.ini` in the root folder using the template in `example.config.ini`
- Configure mailgun as described in `Email notifications setup`
- Build the docker image as in `Docker deployment`
- Enjoy!

### Email notifications setup

- Head to mailgun.com, sign up and confirm your email address
- Go to the `Domain` tab and copy the domain to your configuration file
- Click on your domain and copy the api key to your configuration file

### Docker deployment

In order to deploy the tool with docker build the image with the following command:

```bash
docker build . -t passaporto-checker
```

After the image is built run a container from the root folder with this command:

```bash
docker run -d --name passaporto -v $(pwd):/usr/workspace:rw passaporto-checker
```