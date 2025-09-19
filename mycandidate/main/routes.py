import logging
from flask import request, render_template
from main.app import app

logger = logging.getLogger(__name__)

# Shared default config
DEFAULT_CONFIG = {
    "title": "MyCandidate Demo",
    "footer_colour": "#222222",
    "nav_bars_colour": "#333333",
    "candidate_names_colour": "#007bff",
    "find_candidates_button": "#28a745",
    "logo_colour": "#800080",
    "body_background_colour": "#f8f9fa",
    "body_foreground_colour": "#ffffff",
}

class DummyForm:
    """Stub form class to prevent Jinja template errors"""
    def __init__(self):
        self.csrf_token = ""
    
    def hidden_tag(self):
        return ""
    
    def ds_id(self, **kwargs):
        class_attr = kwargs.get('class', '')
        id_attr = kwargs.get('id', '')
        return f'<select class="{class_attr}" id="{id_attr}" name="ds_id"><option value="">Select an option</option></select>'

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Homepage route (safe stub version).
    Always provides fallback data so Jinja doesn't break.
    """
    try:
        config = DEFAULT_CONFIG

        # Create form stubs for each candidate type
        national_form = DummyForm()
        provincial_form = DummyForm()

        # Minimal sample "data" (mimics ballot categories)
        data = [
            {"candidate_type": "national", "form": national_form},
            {"candidate_type": "provincial", "form": provincial_form},
        ]

        # Stub example candidates
        presidential_candidates = [
            {
                "full_names": "Alice", 
                "surname": "Smith", 
                "party": "Party A", 
                "age": 45,
                "locator": "{location1,code1}"
            }
        ]
        party_members = [
            {
                "full_names": "Bob", 
                "surname": "Jones", 
                "party": "Party A", 
                "age": 50, 
                "orderno": 2
            }
        ]
        candidate = {
            "full_names": "Alice",
            "surname": "Smith",
            "party": "Party A",
            "candidate_type": "national",
            "list_type": "National List",
            "age": 45,
        }

        return render_template(
            "home.html",
            config=config,
            data=data,
            area_name="national",
            candidates=party_members,
            presidential_candidates=presidential_candidates,
            candidate=candidate,
            ward="National",
            form_url="/",
            domain=request.url_root,
        )
    except Exception as e:
        logger.error(f"Home route failed: {e}", exc_info=True)
        return "<h1>Error loading page</h1>", 500


@app.route("/insights", methods=["GET"])
def insights():
    """
    Insights page route.
    Always passes safe defaults.
    """
    try:
        config = DEFAULT_CONFIG
        return render_template(
            "insights.html",
            config=config,
            domain=request.url_root,
            data=[{"candidate_type": "national"}],
            candidate={"candidate_type": "national", "list_type": "National List"},
            presidential_candidates=[],
            candidates=[],
            area_name="national",
        )
    except Exception as e:
        logger.error(f"Insights route failed: {e}", exc_info=True)
        return "<h1>Error loading insights</h1>", 500