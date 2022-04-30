from typing import Any

from rich.console import Console
from rich.table import Table


def print_no_header_table(title: str, data: dict[str, Any]) -> None:
    table = Table(title=f"[red]{title}[/red]", show_header=False)

    for key, val in data.items():
        key_str = f"[green]{key}[/green]"
        match val:
            case tuple() | list() | set() as seq:
                row_str = "\n[green]-[/green] ".join(seq)
                table.add_row(key_str, f"[green]-[/green] {row_str}")
            case _:
                table.add_row(key_str, val)

    console = Console()
    console.print(table)
