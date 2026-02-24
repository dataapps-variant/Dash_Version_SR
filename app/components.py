"""
Shared UI components for all Variant Analytics dashboards.

Usage in any dashboard:
    from app.components import grid_section

    # Replaces the _section_title(...) + dag.AgGrid(...) pair with a
    # fullscreen-capable wrapper. The global MutationObserver in app.py
    # automatically injects the SVG fullscreen button into the title row.
    grid_section("My Report Title", my_dag_grid, "my-grid-id", colors)
"""

from dash import html


def grid_section(title, grid_component, container_id, colors):
    """
    Wrap an AG Grid table with a fullscreen-capable title row.

    The global MutationObserver registered in app.py watches for elements
    with class 'vg-grid-fs-title' and automatically injects the SVG
    fullscreen/exit button at the right end of the title row.
    No additional Dash callbacks or IDs are required.

    Args:
        title (str):            Section header text (e.g. "Spend Pacing: Actual vs Target (MTD)")
        grid_component:         A dag.AgGrid component (or any component to wrap)
        container_id (str):     Base ID — the wrapper div gets id="{container_id}-fs-wrapper"
        colors (dict):          Theme colors dict from get_theme_colors()

    Returns:
        html.Div: Title row + grid wrapped in a fullscreen-capable container.

    Notes:
        - Works automatically in any dashboard — no per-dashboard JS needed.
        - For Plotly charts (dcc.Graph), fullscreen is handled separately by
          the same MutationObserver watching for .js-plotly-plot elements.
        - To add fullscreen to a new dashboard's grids, just import this
          function and use it in place of the _section_title + grid pair.
    """
    return html.Div(
        [
            # Title row — the MutationObserver injects the ⛶ button here
            html.Div(
                html.Span(
                    title,
                    style={
                        "color": colors["text_primary"],
                        "fontWeight": "600",
                        "fontSize": "14px",
                    },
                ),
                className="vg-grid-fs-title",
            ),
            # The grid itself
            grid_component,
        ],
        id=f"{container_id}-fs-wrapper",
        className="vg-grid-fs-wrapper",
    )
