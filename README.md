# Matterbridge Auto-Config

App that generates a Matterbridge config file based on channel names.

This remote configuration file\* is generated based on simple
channel-naming rules.

<sup>NOTE: This app is based on features that are not yet implemented or
merged into Matterbridge. Unimplemented features are notes with an
asterisk*.<.sup>

## Features

- Supports: Slack
- Creates translation gateways\* based on language-code suffix
- Forces Matterbridge config reload when remote config\* changes

## Usage

Once you've got this app running and configured:

- Add a two-letter language suffix to a channel will set the locale of
  that channel. This will allow Matterbridge to translate incoming
messages into the target language, assuming the Google Translation
feature is enabled\*.
  - Example: `#mychannel-en`
  - This feature requires that a "base channel" exists (eg.
    `#mychannel`), which will have all untranslated messages dropped
  into it. This ensures that team members who speak multiple languages
  won't be forced to read imperfect Google Translations.

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

## Configuration

Configuration is done via environment variables. See
[`sample.env`](sample.env) for
details. If a `.env` file is present, its values will be used
automatically.

### `SLACK_API_TOKEN` (Required)

The API token from your Slack team.

You may use [**legacy user tokens**][legacy-tokens] or [**bot
tokens**][bot-tokens]. We recommend bot tokens, or otherwise the token
will have access to all the user's private conversations. Also, a bot
must be invited into each channel or conversation, which is added
precaution in case your token gets released into the wild.

### `TEMPLATE_URL` (Optional)

The URL of a template file that will wrap the auto-generated portion of
your configuration. The string `{{AUTOGENERATED}}` will be replaced.

See
[`examples/matterbridge.sample.toml`](examples/matterbridge.sample.toml).

## `OUTGOING_WEBHOOK_URL` and `OUTGOING_WEBHOOK_TOKEN` (Recommended)

The full url of the `/webhook` endpoint enabled on your Matterbridge
instance\*, used to prompt Matterbridge to reload remote configuration.
When channel events are detected on Slack, this autoconfig app will use
this endpoint to prompt a reload of the remotely hosted configuration.

The auth token must match the one configured in Matterbridge.

## Deployment

We host a [version of this on Heroku][demo]. Here are the details:

- `master` branch is automatically deployed there.
- All changes are made throgh pull requests.

## Future Plans

- [x] Serve as a flask webapp
- [x] Use template via base64 envvar or url
- [ ] Configure tokens via envvar (upstream in Matterbridge)
- [ ] Listen for channel updates and regenerate config
- [ ] POST to Matterbridge endpoint to trigger reload (upstream in
  Matterbridge)

   [pipenv]: https://pipenv.readthedocs.io/en/latest/
   [pyenv]: https://github.com/pyenv/pyenv
   [demo]: https://matterbridge-autoconfig-g0vtw.herokuapp.com/
   [legacy-tokens]: https://api.slack.com/custom-integrations/legacy-tokens
   [bot-tokens]: https://my.slack.com/apps/new/A0F7YS25R-bots

