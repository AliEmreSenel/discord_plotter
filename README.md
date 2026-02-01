# Discord Plotter

A lightweight Python module designed to send Matplotlib figures directly to a Discord channel using Webhooks.

## Features

- **Lightweight**: Minimal dependencies (`requests`, `matplotlib`, `python-dotenv`).
- **Clean**: No temporary file cleanup required.
- **Secure**: Webhook URLs are managed via environment variables.

## Installation

```bash
uv add git+https://github.com/AliEmreSenel/discord_plotter.git
```

or

```bash
uv add git+ssh://git@github.com/AliEmreSenel/discord_plotter.git
```

## Configuration

This module requires a **Discord Webhook URL**.

1. In Discord, go to **Server Settings** > **Integrations** > **Webhooks**.
2. Create a Webhook and copy the URL.
3. Set the `DISCORD_WEBHOOK_URL` environment variable.

### Option A: Using a `.env` file (Recommended)

Create a file named `.env` in the folder where you run your script:

```ini
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_id/your_token
```

### Option B: Using Terminal Export

```bash
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/your_id/your_token"

```
