---
layout: use_case
title: "Recto/Verso"
description: |
  A full page that aligns front and back. This use case represents documents where both sides of a page contain content that should be viewed and aligned together, such as a manuscript page with text on both sides or a document with illustrations on both the front (recto) and back (verso) of a single leaf.
  
  The challenge is to present both sides in a way that allows viewers to understand the spatial relationship between the two sides and potentially see through translucent materials or align watermarks, damage, and other features visible from both sides.
examples: |
  A typical example would be a playing card, where the front side (recto) displays the card's value and suit, while the back side (verso) features a decorative pattern. Both sides are integral to the card's identity and use.
  
  Another example is a watercolor painting on thin paper where the paint has bled through to the reverse side, creating a secondary image that complements the primary artwork.
instances:
  - title: "A great example here!"
    url: "#nothing"
    description: "A 15th-century manuscript with text and illuminations on both recto and verso sides"
links:
  - title: "IIIF Presentation API 3.0"
    url: "https://iiif.io/api/presentation/3.0/"
  - title: "IIIF Image API"
    url: "https://iiif.io/api/image/3.0/"
data:
  manifest: "https://cubap.github.io/movable-books/fixtures/manifests/all.json"
---

## Additional Context

The recto/verso use case is fundamental to understanding double-sided documents in digital collections. This pattern can be extended to more complex scenarios involving multiple layers or transparent overlays.

## Implementation Notes

When implementing recto/verso views, consider:
- Providing a toggle or flip animation to switch between sides
- Offering a side-by-side comparison view
- Indicating which side is currently being viewed
- Maintaining consistent orientation and scale between views
