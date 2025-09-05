# DevOps Slack Bot

A lightweight Slack bot that listens to messages in a Slack workspace and triggers deployment pipelines via a Jenkins‑like API.  The application demonstrates ChatOps and DevOps automation integration using microservices orchestrated by Docker Compose.

## Features

* Parse Slack events and identify deployment commands.
* Invoke a pipeline trigger endpoint on an internal Jenkins service to start builds.
* Respond back to Slack with the status of the requested deployment.
* Run multiple services under Docker Compose for easy local development.

## Tech Stack

* **Python** with **Flask** for handling HTTP requests from Slack and dispatching actions.
* **Slack Bolt** SDK for parsing events and verifying signatures.
* **Requests** for interacting with the Jenkins API.
* **Docker Compose** to orchestrate the bot and a mocked Jenkins service.

## Usage

1. Set the following environment variables in a `.env` file or your shell: `SLACK_BOT_TOKEN`, `SLACK_SIGNING_SECRET`, `JENKINS_USER`, `JENKINS_TOKEN`.
2. Run `docker compose up --build` from the project root.
3. Expose the `/slack/events` endpoint publicly with a tool such as ngrok and configure a Slack Events subscription pointing to it.
4. In Slack, send a message like `deploy my‑service` in a channel the bot is a member of.  The bot will call the Jenkins service and report the trigger status.
