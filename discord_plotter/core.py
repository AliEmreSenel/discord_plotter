import os
import io
import tempfile
import requests
from matplotlib.figure import Figure
from matplotlib.animation import Animation
from dotenv import load_dotenv

load_dotenv()


def send_plot(plot_object, description="Here is your plot", filename=None):
    """
    Sends a matplotlib Figure or Animation to a Discord webhook.

    Args:
        plot_object: A matplotlib.figure.Figure OR matplotlib.animation.Animation.
        description (str): The text message to accompany the image.
        filename (str, optional): Custom filename. Defaults to 'plot.png' or 'animation.gif'.

    Raises:
        ValueError: If DISCORD_WEBHOOK_URL is not set or input type is invalid.
    """
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        raise ValueError("Environment variable 'DISCORD_WEBHOOK_URL' is not set.")

    buffer = io.BytesIO()

    if isinstance(plot_object, Animation):
        fname = filename or "animation.gif"
        mime_type = "image/gif"

        fd, temp_path = tempfile.mkstemp(suffix=".gif")
        os.close(fd)

        try:
            plot_object.save(temp_path, writer="pillow", fps=2)

            with open(temp_path, "rb") as f:
                buffer.write(f.read())
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    elif isinstance(plot_object, Figure):
        fname = filename or "plot.png"
        mime_type = "image/png"
        plot_object.savefig(buffer, format="png", bbox_inches="tight")
    else:
        raise TypeError(
            f"Expected matplotlib Figure or Animation, got {type(plot_object)}"
        )

    buffer.seek(0)

    payload = {"content": description}

    files = {"file": (fname, buffer, mime_type)}

    try:
        response = requests.post(webhook_url, data=payload, files=files)
        response.raise_for_status()
        print(
            f"Successfully sent {fname} to Discord. Status Code: {response.status_code}"
        )
    finally:
        buffer.close()
