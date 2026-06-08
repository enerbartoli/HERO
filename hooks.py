"""
MkDocs hook — injects hero_bg_url and hero_label into each page's
template context so docs/overrides/main.html can render section banners.

Section → asset mapping follows BRAND_ASSETS.md:
  heroic characters (Transformers, D&D) on lead sections;
  non-hero franchises (Monopoly, Peppa, Play-Doh) on back sections;
  plain gradients for dense reference pages.
"""

_SECTION_MAP = [
    # (url_prefix_or_empty,  asset_path,                        label)
    ("roles/",              "assets/img/hero-bumblebee.jpg",   "Role-based guides"),
    ("getting-started/",    "assets/img/hero-dnd.jpg",         "Getting started"),
    ("tools/",              "assets/img/bg-gradient-1.jpg",    "Tools & templates"),
    ("workflows/",          "assets/img/bg-gradient-2.jpg",    "Workflows"),
    ("examples/",           "assets/img/hero-playdoh.jpg",     "Examples"),
    ("help/",               "assets/img/hero-peppa.jpg",       "Help & troubleshooting"),
    ("reference/",          "assets/img/hero-monopoly.jpg",    "Reference"),
]

_HOME_IMAGE = "assets/img/hero-transformers.jpg"
_HOME_LABEL = "HERO User Manual"


def on_page_context(context, page, config, nav, **kwargs):
    url = page.url or ""

    # Compute how many directory levels deep the page is so we can
    # build a root-relative path for the background-image CSS value.
    # e.g. "roles/demand-planner/" has 2 slashes → prefix = "../../"
    depth = url.count("/")
    rel_prefix = "./" if depth == 0 else "../" * depth

    # Match section
    hero_img = None
    hero_lbl = None

    stripped = url.strip("./")
    if not stripped:                          # home / root
        hero_img = _HOME_IMAGE
        hero_lbl = _HOME_LABEL
    else:
        for prefix, img, lbl in _SECTION_MAP:
            if url.startswith(prefix):
                hero_img = img
                hero_lbl = lbl
                break

    if hero_img:
        context["hero_bg_url"] = rel_prefix + hero_img
        context["hero_label"]  = hero_lbl
    else:
        context["hero_bg_url"] = None
        context["hero_label"]  = None

    return context
