from pathlib import Path
import json

from viktor.parametrization import ViktorParametrization
from viktor.utils import render_jinja_template
from viktor.views import WebView, WebResult
from viktor import ViktorController

class Parametrization(ViktorParametrization):
    pass


class Controller(ViktorController):
    label = 'My Entity Type'
    parametrization = Parametrization

    @WebView("What's next?", duration_guess=1)
    def whats_next(self, **kwargs):
        """Initiates the process of rendering the "What's next?" tab."""
        html_path = Path(__file__).parent / "info_page" / "html_template.html"
        input_path = Path(__file__).parent / "info_page" / "info_input.json"
        with input_path.open() as f:
            input_path = json.load(f)
        with open(html_path, 'rb') as template:
            html_file = render_jinja_template(template, input_path)
        html_path = Path(__file__).parent / "info_page" / "html_sample.html"
        with open(html_path, 'w') as sample:
            sample.write(html_file.getvalue())
        return WebResult(html=html_file.getvalue())