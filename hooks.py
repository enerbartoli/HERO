"""
MkDocs hook — injects hero banner context into each page so that
docs/overrides/main.html can render a section banner with:
  * a hero background image,
  * a Hasbro brand-logo badge (transparent .webp accent),
  * subtle pattern + light-streak SVG texture overlays,
  * the section label.

Brand mapping rationale:
  - heroic characters (Transformers, D&D) lead the most visible sections;
  - non-hero franchises (Monopoly, Play-Doh, Peppa) sit on back sections;
  - dense sections (Tools, Workflows) use character-free gradients;
  - each section is paired with a Hasbro-OWNED brand logo as an accent.

Partner brands (marvel-logo, star-wars-logo) are intentionally NOT used
for primary branding — they are Disney/Lucasfilm IP.
"""

# (url_prefix, hero_image, brand_logo, label)
_SECTION_MAP = [
    ("roles/",           "assets/img/hero-bumblebee.jpg",  "assets/img/brands/transformers-logo.webp",        "Role-based guides"),
    ("getting-started/", "assets/img/hero-dnd.jpg",        "assets/img/brands/dnd-logo.webp",                 "Getting started"),
    ("tools/",                              "assets/img/bg-gradient-1.jpg",   "assets/img/brands/nerf-logo.webp",                "Tools & templates"),
    ("workflows/forecast-range-calculation", "assets/img/bg-gradient-2.jpg",   "assets/img/brands/magic-the-gathering-logo.webp", "Forecast Calculation Range & Disaggregation"),
    ("workflows/",                           "assets/img/bg-gradient-2.jpg",   "assets/img/brands/magic-the-gathering-logo.webp", "Workflows"),
    ("examples/",        "assets/img/hero-playdoh.jpg",    "assets/img/brands/playdoh-logo.webp",             "Examples"),
    ("help/",            "assets/img/hero-peppa.jpg",      "assets/img/brands/my-little-pony-logo.webp",      "Help & troubleshooting"),
    ("reference/",       "assets/img/hero-monopoly.jpg",   "assets/img/brands/monopoly-logo.webp",            "Reference"),
]

_HOME_IMAGE = "assets/img/hero-transformers.jpg"
_HOME_LOGO  = "assets/img/brands/transformers-logo.webp"
_HOME_LABEL = "HERO User Manual"

_PATTERN = "assets/img/pattern-frames.svg"
_STREAKS = "assets/img/light-streaks.svg"


def on_page_context(context, page, config, nav, **kwargs):
    url = page.url or ""

    # Root-relative prefix so background-image / src resolve from any depth.
    # e.g. "roles/demand-planner/" has 2 slashes → prefix = "../../"
    depth = url.count("/")
    rel_prefix = "./" if depth == 0 else "../" * depth

    hero_img = None
    hero_logo = None
    hero_lbl = None

    if not url.strip("./"):                       # home / root
        hero_img, hero_logo, hero_lbl = _HOME_IMAGE, _HOME_LOGO, _HOME_LABEL
    else:
        for prefix, img, logo, lbl in _SECTION_MAP:
            if url.startswith(prefix):
                hero_img, hero_logo, hero_lbl = img, logo, lbl
                break

    if hero_img:
        context["hero_bg_url"]      = rel_prefix + hero_img
        context["hero_logo_url"]    = rel_prefix + hero_logo
        context["hero_label"]       = hero_lbl
        context["hero_pattern_url"] = rel_prefix + _PATTERN
        context["hero_streaks_url"] = rel_prefix + _STREAKS
    else:
        context["hero_bg_url"]      = None
        context["hero_logo_url"]    = None
        context["hero_label"]       = None
        context["hero_pattern_url"] = None
        context["hero_streaks_url"] = None

    return context
