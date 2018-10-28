# Matterbridge Auto-Config

App that generates a Matterbridge config file based on channel names.

Right now it's just a CLI script, but will be a web app eventually.

## Features

- Supports: Slack
- Creates translation gateways based on language-code suffix

## :computer: Local Development

We recommend using [`pipenv`][pipenv] and [`pyenv`][pyenv] to manage
development environments.

```
pipenv install
EXPORT SLACK_API_TOKEN=xoxx-1234567890...
pipenv run python generate.py
```

## Deployment

We host a version of this on Heroku. Here are the details:

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

