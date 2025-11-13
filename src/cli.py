import click
import preprocessing as pr

@click.group()
def cli():
    """General CLI group for data preprocessing utilities."""
    pass

# CLEAN GROUP
@cli.group(help="Data cleaning functions")
def clean():
    pass

@clean.command(help="Remove missing values (None, '', nan). Example: cli clean remove-missing 1 '' nan 2")
@click.argument("values", nargs=-1)
def remove_missing_cmd(values):
    click.echo(pr.remove_missing(values))

@clean.command(help="Fill missing values with a given value. Example: cli clean fill-missing 1 '' nan 2 --fill-value 0")
@click.argument("values", nargs=-1)
@click.option("--fill-value", default=0, help="Value to replace missing entries")
def fill_missing_cmd(values, fill_value):
    click.echo(pr.fill_missing(values, fill_value))

# NUMERIC GROUP
@cli.group(help="Numerical attribute functions")
def numeric():
    pass

@numeric.command(help="Normalize values with min-max scaling. Example: cli numeric normalize 10 20 30 --new-min 0 --new-max 1")
@click.argument("values", nargs=-1, type=float)
@click.option("--new-min", default=0.0, help="New minimum value")
@click.option("--new-max", default=1.0, help="New maximum value")
def normalize_cmd(values, new_min, new_max):
    click.echo(pr.normalize_minmax(values, new_min, new_max))

@numeric.command(help="Standardize values with z-score. Example: cli numeric standardize 10 20 30")
@click.argument("values", nargs=-1, type=float)
def standardize_cmd(values):
    click.echo(pr.standardize_zscore(values))

@numeric.command(help="Clip values to a range. Example: cli numeric clip 1 5 10 --min-val 2 --max-val 8")
@click.argument("values", nargs=-1, type=float)
@click.option("--min-val", default=0.0, help="Minimum clip value")
@click.option("--max-val", default=1.0, help="Maximum clip value")
def clip_cmd(values, min_val, max_val):
    click.echo(pr.clip_values(values, min_val, max_val))

@numeric.command(help="Convert values to integers. Example: cli numeric to-int 1 2.5 abc 3")
@click.argument("values", nargs=-1)
def to_int_cmd(values):
    click.echo(pr.convert_to_int(values))

@numeric.command(help="Logarithmic transform of positive values. Example: cli numeric log-transform 1 10 100")
@click.argument("values", nargs=-1, type=float)
def log_transform_cmd(values):
    click.echo(pr.log_transform(values))

# TEXT GROUP
@cli.group(help="Text processing functions")
def text():
    pass

@text.command(help="Tokenize text into words. Example: cli text tokenize 'Hello World 123!'")
@click.argument("text")
def tokenize_cmd(text):
    click.echo(pr.tokenize_text(text))

@text.command(help="Remove punctuation from text. Example: cli text clean 'Hello!! World??'")
@click.argument("text")
def clean_cmd(text):
    click.echo(pr.clean_text(text))

@text.command(help="Remove stopwords from text. Example: cli text remove-stopwords 'this is a test' --stopwords is a")
@click.argument("text")
@click.option("--stopwords", multiple=True, help="Stopwords to remove")
def remove_stopwords_cmd(text, stopwords):
    click.echo(pr.remove_stopwords(text, set(stopwords)))

# STRUCT GROUP
@cli.group(help="Structural data functions")
def struct():
    pass

@struct.command(help="Shuffle values with optional seed. Example: cli struct shuffle 1 2 3 4 --seed 42")
@click.argument("values", nargs=-1)
@click.option("--seed", type=int, default=None, help="Seed for reproducibility")
def shuffle_cmd(values, seed):
    click.echo(pr.shuffle_list(list(values), seed))

@struct.command(help="Flatten a list of lists. Example: cli struct flatten '[1,2]' '[3,4]'")
@click.argument("lists", nargs=-1)
def flatten_cmd(lists):
    # naive eval for demo purposes
    parsed = [eval(l) for l in lists]
    click.echo(pr.flatten_list(parsed))

@struct.command(help="Remove duplicate values. Example: cli struct unique 1 2 2 3")
@click.argument("values", nargs=-1)
def unique_cmd(values):
    click.echo(pr.remove_duplicates(values))

# ----------------------------
# Entry point
# ----------------------------
if __name__ == "__main__":
    cli()
