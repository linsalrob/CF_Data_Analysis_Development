# Green box helper for Jupyter (written by ChatGPT)

from IPython.display import HTML, display
import html

def green_box(message, title=None, width=None, icon=True, raw_html=False):
    """
    Render a green message box in Jupyter output.
    
    Parameters
    ----------
    message : str
        The main message to render. Newlines are converted to <br>.
    title : str, optional
        Bold heading shown above the message.
    width : str or int, optional
        Max width for the box (e.g., '600px', '40em', '80%', or an int like 600).
        If None, it will stretch to fit the container.
    icon : bool, default True
        If True, add a checkmark icon before the title.
    raw_html : bool, default False
        If True, treat `message` as raw HTML (no escaping). Use carefully.
    """
    # Determine the width CSS
    if width is None:
        width_css = "none"
    elif isinstance(width, int):
        width_css = f"{width}px"
    else:
        width_css = str(width)
    
    # Escape or pass-through content
    if not raw_html:
        message_html = html.escape(str(message)).replace("\n", "<br>")
        title_html = html.escape(str(title)) if title else None
    else:
        message_html = str(message)
        title_html = str(title) if title else None

    # Optional icon
    icon_html = "✅ " if icon and title_html else ""

    # Optional title block
    title_block = (
        f'<div style="font-weight:600; margin-bottom:4px;">{icon_html}{title_html}</div>'
        if title_html else ""
    )

    # Core style (Bootstrap-ish success palette)
    style = (
        "background-color:#d4edda;"
        "border:1px solid #155724;"
        "color:#155724;"
        "padding:10px 12px;"
        "border-radius:8px;"
        "font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;"
        "line-height:1.4;"
        f"max-width:{width_css};"
    )
    
    box_html = f'<div style="{style}">{title_block}<div>{message_html}</div></div>'
    return HTML(box_html)

def show_green(message, **kwargs):
    """Display a green box immediately (wrapper around green_box + display)."""
    display(green_box(message, **kwargs))
