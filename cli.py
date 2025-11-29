"""
Command-line interface for the Python Test Repository.
"""

import click
import logging
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from config import get_config
from data_analysis import generate_sample_data, calculate_metrics
from utils import DataProcessor

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Python Test Repository CLI - Utilities and data operations."""
    pass


@cli.command()
@click.option('--rows', default=10, help='Number of rows to generate')
@click.option('--output', '-o', help='Output file path (optional)')
def generate(rows, output):
    """Generate sample data."""
    console.print(f"[bold blue]Generating {rows} rows of sample data...[/bold blue]")
    
    df = generate_sample_data(rows)
    
    # Display in table
    table = Table(title="Sample Data Preview (first 5 rows)")
    for col in df.columns:
        table.add_column(col, style="cyan")
    
    for _, row in df.head(5).iterrows():
        table.add_row(*[str(val) for val in row])
    
    console.print(table)
    
    if output:
        df.to_csv(output, index=False)
        console.print(f"[bold green]✓[/bold green] Data saved to {output}")
    
    # Show metrics
    metrics = calculate_metrics(df, 'value')
    console.print("\n[bold]Value Column Metrics:[/bold]")
    for key, value in metrics.items():
        console.print(f"  {key}: {value:.2f}")


@cli.command()
@click.argument('email')
def validate(email):
    """Validate an email address."""
    from utils import validate_email
    
    is_valid = validate_email(email)
    
    if is_valid:
        console.print(f"[bold green]✓[/bold green] '{email}' is a valid email address")
    else:
        console.print(f"[bold red]✗[/bold red] '{email}' is not a valid email address")


@cli.command()
def info():
    """Display application information."""
    config = get_config()
    
    table = Table(title="Application Information")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("App Name", config.APP_NAME)
    table.add_row("Version", config.APP_VERSION)
    table.add_row("Debug Mode", str(config.DEBUG))
    table.add_row("Database Host", config.DB_HOST)
    table.add_row("MongoDB URI", config.MONGO_URI)
    table.add_row("Redis Host", f"{config.REDIS_HOST}:{config.REDIS_PORT}")
    
    console.print(table)


@cli.command()
@click.option('--count', default=5, help='Number of test items')
def process(count):
    """Process test data."""
    console.print(f"[bold blue]Processing {count} items...[/bold blue]")
    
    processor = DataProcessor()
    
    # Generate test data
    test_data = [{'id': i, 'name': f'Item {i}', 'value': i * 10} for i in range(1, count + 1)]
    
    # Process
    processed = processor.process_data(test_data)
    
    console.print(f"[bold green]✓[/bold green] Processed {len(processed)} items")
    console.print(f"Total processed count: {processor.processed_count}")


if __name__ == '__main__':
    cli()
