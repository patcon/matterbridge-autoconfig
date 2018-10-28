# Matterbridge Auto-Config

App that generates a Matterbridge config file based on channel names.

Right now it's just a CLI script, but will be a web app eventually.

## Features

- Supports: Slack
- Creates translation gateways based on language-code suffix

## :computer: Local Development

### Setup

We recommend using [`pipenv`][pipenv] and [`pyenv`][pyenv] to manage
development environments.

```
pipenv install
cp sample.env .env
# Add your Slack API token here:
vim .env
```

### Running

On the command line:

```
pipenv run python cli.py
```

Or, for the web app:

```
pipenv run python app.py
```

## Deployment

We host a [version of this on Heroku][demo]. Here are the details:

- `master` branch is automatically deployed there.
- All changes are made throgh pull requests.

## Future Plans

- [ ] Serve as a flask webapp
- [ ] Use template via base64 envvar or url
- [ ] Configure tokens via envvar (upstream in Matterbridge)
- [ ] Listen for channel updates and regenerate config
- [ ] POST to Matterbridge endpoint to trigger reload (upstream in
  Matterbridge)

   [pipenv]: https://pipenv.readthedocs.io/en/latest/
   [pyenv]: https://github.com/pyenv/pyenv
   [demo]: https://matterbridge-autoconfig-g0vtw.herokuapp.com/

