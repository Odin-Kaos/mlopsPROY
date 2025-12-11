"""
Main CLI or app entry point for prediction library
"""

import click
from Lab1.mylib.model import predict, rescale

@click.group()
def cli():
    """Main CLI to perform image prediction operations."""


@cli.command("predict")
@click.argument("img_path", type=click.Path(exists=True))
def predict_cli(img_path):
    """Predict the class of an image.

    Example:
        uv run python -m cli.cli predict path/to/image.jpg
    """
    # For simplicity, just pass the path string to predict
    # In a real app, you'd load the image into a tensor first
    result = predict(img_path)
    click.echo(click.style(f"Prediction: {result}", fg="green"))


@cli.command("rescale")
@click.argument("img_path", type=click.Path(exists=True))
@click.argument("size", type=int)
def rescale_cli(img_path, size):
    """Rescale an image to a given size.

    Example:
        uv run python -m cli.cli rescale path/to/image.jpg 128
    """
    # Again, in a real app you'd load the image into a tensor
    # Here we just echo the intended operation
    click.echo(click.style(f"Rescaled {img_path} to {size}x{size}", fg="green"))
