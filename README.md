# CI Agent Simulator

This repository simulates periodic telemetry agents using GitHub Actions. It is designed to emulate how distributed runners collect and forward runtime metadata over time.

## 📦 Features

- Agent setup and environment bootstrapping
- Delayed randomized execution windows
- Log generation and structured parsing
- Telegram-based status notifier
- Automatic self-retriggering for long-term runtime simulation

## 📁 Workflow Overview

The workflow mimics real-world background tasks and is useful for:

- CI pipeline runtime benchmarks
- Scheduling & retrigger logic verification
- Lightweight telemetry agent simulations
- Monitoring tool testbeds

## 🔄 Runtime Behavior

- Runs for 20–90 minutes per session
- Adds randomized initial delay (30s–5min)
- Sends summary log to Telegram after run
- Sleeps before re-triggering next session
- Designed to simulate ephemeral CI tasks

## ⚠️ Disclaimer

This repository does **not handle any sensitive data**. All execution is performed in ephemeral runners provided by GitHub. Intended for **educational and simulation** purposes only.

## 📬 Maintained by

EndiHariadi43 – Passionate about CI systems, log parsing, and performance testing automation.

License: MIT
