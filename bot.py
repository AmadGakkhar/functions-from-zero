#!/usr/bin/env python
from utils.funcs import wiki_summary

import click

@click.command()
@click.option('--name', default='Microsoft', help='Page Name.')
@click.option('--lines', prompt='Number of Lines',
              help='The number of lines in the summary.')
def cli(name, lines):
    """Wikipedia bot which visits the specified page and summarizes it."""
    
    click.echo(f"{wiki_summary(name, lines)}!")

if __name__ == '__main__':
    cli()