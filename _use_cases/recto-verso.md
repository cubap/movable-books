---
layout: use_case
title: "Recto/Verso"
description: |
  A full page that aligns front and back. This use case represents documents where both sides of a page contain content that should be viewed and aligned together, such as a manuscript page with text on both sides or a document with illustrations on both the front (recto) and back (verso) of a single leaf.
  
  The challenge is to present both sides in a way that allows viewers to understand the spatial relationship between the two sides and potentially see through translucent materials or align watermarks and other features visible from both sides.
examples: |
  A typical example would be a medieval manuscript where the scribe wrote on both sides of a vellum leaf. When studying the manuscript, scholars may need to see both sides simultaneously to understand corrections, annotations, or artistic elements that span both surfaces.
  
  Another example is a watercolor painting on thin paper where the paint has bled through to the reverse side, creating a secondary image that complements the primary artwork.
instances:
  - title: "Medieval Manuscript Folio"
    url: "#"
    description: "A 15th-century manuscript with text and illuminations on both recto and verso sides"
  - title: "Japanese Woodblock Print"
    url: "#"
    description: "A double-sided print where the verso contains artist's notes and sketches"
links:
  - title: "IIIF Presentation API 3.0"
    url: "https://iiif.io/api/presentation/3.0/"
  - title: "IIIF Image API"
    url: "https://iiif.io/api/image/3.0/"
data:
  manifest: |
    {
      "@context": "http://iiif.io/api/presentation/3/context.json",
      "id": "https://example.org/iiif/book1/manifest",
      "type": "Manifest",
      "label": { "en": [ "Recto/Verso Example" ] },
      "items": [
        {
          "id": "https://example.org/iiif/book1/canvas/p1",
          "type": "Canvas",
          "label": { "en": [ "Page 1" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/book1/page/p1/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/book1/annotation/p1-recto",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/book1/recto.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/book1/canvas/p1"
                }
              ]
            }
          ]
        },
        {
          "id": "https://example.org/iiif/book1/canvas/p1-verso",
          "type": "Canvas",
          "label": { "en": [ "Page 1 (verso)" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/book1/page/p1-verso/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/book1/annotation/p1-verso",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/book1/verso.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/book1/canvas/p1-verso"
                }
              ]
            }
          ]
        }
      ]
    }
---

## Additional Context

The recto/verso use case is fundamental to understanding double-sided documents in digital collections. This pattern can be extended to more complex scenarios involving multiple layers or transparent overlays.

### Implementation Notes

When implementing recto/verso views, consider:
- Providing a toggle or flip animation to switch between sides
- Offering a side-by-side comparison view
- Indicating which side is currently being viewed
- Maintaining consistent orientation and scale between views
