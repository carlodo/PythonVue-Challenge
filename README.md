# Moti

## Mission Statement

To inspire individuals to find meaning in work.


## Description

Moti is an app that allows teams to gain awareness of their motivation level
through Self-Determination Theory (SDT).

A team leader, or _motiveer_, invites his team of _motivees_ to participate
in a survey. Moti then provides motiveers with insights into team engagement
and motivation through automated data analysis and meaningful visualizations.

Motiveers:
  - Create organization account,
  - Enter email addresses of motivees,
  - Hit send,
  - View results of automated data analysis.
Motivees:
  - Click link,
  - Answer questions on any browser,
  - (MVP++: View their motivation profile).


### Functionalities
  - Setup must be hassle-free,
  - Answering the survey must be hassle-free,
  - App runs on any mobile or desktop browser,
  - App is GDPR compliant.


## Build Setup

### Set up environment

``` bash
cp .env.sample .env
openssl rand -hex 64 > .authkey
```

### Build docker containers

To serve with backend/frontend hot reload at localhost:80:

``` bash
docker-compose up
```

## Code Style

- Python sources follow the PEP8 style guide.
- JavaScript sources follow the `standard` style guide.

To check for code style issues, run

```bash
make lint
```

Equip your code editor with a linter. If you are using neovim, `ale` can be
configured to run `pylama` for python sources, and `eslint` for javascript/vue
sources.
