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

# (url_prefix, hero_image, brand_logo, label, variant)
#   variant=None  → standard photo banner (navy gradient overlay + texture + logo)
#   variant="art" → self-contained branded artwork shown as-is: no navy overlay,
#                   no texture, no franchise logo; label sits on the light side.
_SECTION_MAP = [
    ("roles/",           "assets/img/hero-bumblebee.jpg",  "assets/img/brands/transformers-logo.webp",        "Role-based guides",            None),
    ("getting-started/", "assets/img/hero-dnd.jpg",        "assets/img/brands/dnd-logo.webp",                 "Getting started",              None),
    ("tools/",                              "assets/img/bg-gradient-1.jpg",   "assets/img/brands/nerf-logo.webp",                "Tools & templates",            None),
    ("workflows/forecast-range-calculation", "assets/img/hero-gijoe.jpg",       None,                                              "Forecast Calculation Range & Disaggregation", None),
    ("workflows/",                           "assets/img/bg-gradient-2.jpg",   "assets/img/brands/magic-the-gathering-logo.webp", "Workflows",                    None),
    ("examples/",        "assets/img/hero-playdoh.jpg",    "assets/img/brands/playdoh-logo.webp",             "Examples",                     None),
    ("help/",            "assets/img/hero-peppa.jpg",      "assets/img/brands/my-little-pony-logo.webp",      "Help & troubleshooting",       None),
    ("reference/",       "assets/img/hero-monopoly.jpg",   "assets/img/brands/monopoly-logo.webp",            "Reference",                    None),
    # Pilot-only section: dedicated H.E.R.O. TOOL brand banner, shown as flat
    # artwork (no navy overlay, no texture, no franchise logo). Unique among
    # all sections.
    ("special-considerations/", "assets/img/hero-special-considerations.jpg", None,                          "Special Considerations During Pilot", "art"),
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
    hero_variant = None

    if not url.strip("./"):                       # home / root
        hero_img, hero_logo, hero_lbl = _HOME_IMAGE, _HOME_LOGO, _HOME_LABEL
    else:
        for prefix, img, logo, lbl, variant in _SECTION_MAP:
            if url.startswith(prefix):
                hero_img, hero_logo, hero_lbl, hero_variant = img, logo, lbl, variant
                break

    # A banner renders whenever a section matched (label is set). The hero
    # image is optional: sections without one fall back to the navy gradient
    # defined in extra.css. The variant controls overlay/texture treatment.
    if hero_lbl:
        context["hero_bg_url"]      = (rel_prefix + hero_img) if hero_img else None
        context["hero_logo_url"]    = (rel_prefix + hero_logo) if hero_logo else None
        context["hero_label"]       = hero_lbl
        context["hero_variant"]     = hero_variant
        context["hero_pattern_url"] = rel_prefix + _PATTERN
        context["hero_streaks_url"] = rel_prefix + _STREAKS
    else:
        context["hero_bg_url"]      = None
        context["hero_logo_url"]    = None
        context["hero_label"]       = None
        context["hero_variant"]     = None
        context["hero_pattern_url"] = None
        context["hero_streaks_url"] = None

    # Always expose rel_prefix so templates can build asset URLs from any depth.
    context["rel_prefix"] = rel_prefix

    return context
