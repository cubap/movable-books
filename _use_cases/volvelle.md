---
layout: use_case
title: "Volvelle"
description: |
  A volvelle is a movable device consisting of one or more rotating discs or wheels, typically made of paper or vellum, that are mounted on a page with a central pivot point. These devices were commonly used in medieval and early modern manuscripts and books for calculations, astronomical observations, divination, or illustrating concepts with multiple layers of information.
  
  The key characteristic is that one or more circular elements can rotate around a fixed anchor point, often with cutout windows or transparent regions that reveal different information as the disc rotates.
examples: |
  A classic example is an astronomical volvelle used to calculate the positions of celestial bodies. The device might have multiple layers:
  - A base layer showing the zodiac signs
  - A middle layer with the months of the year
  - A top layer with a pointer that can be rotated to align dates with zodiac positions
  
  Another example is a medical volvelle showing the relationship between bodily humors, seasons, and treatments, where rotating the disc aligns different combinations of information.
instances:
  - title: "Astronomical Volvelle from Peter Apian"
    url: "https://www.metmuseum.org/art/collection/search/356983"
    description: "16th-century astronomical computing device with rotating paper discs"
  - title: "Medieval Medical Volvelle"
    url: "#"
    description: "A diagnostic tool for determining treatments based on aligned symptoms"
links:
  - title: "Wikipedia: Volvelle"
    url: "https://en.wikipedia.org/wiki/Volvelle"
data:
  manifest: |
    {
      "@context": "http://iiif.io/api/presentation/3/context.json",
      "id": "https://example.org/iiif/volvelle/manifest",
      "type": "Manifest",
      "label": { "en": [ "Volvelle Example" ] },
      "items": [
        {
          "id": "https://example.org/iiif/volvelle/canvas/p1",
          "type": "Canvas",
          "label": { "en": [ "Page with Volvelle" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/volvelle/page/p1/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/volvelle/annotation/base",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/volvelle/base-page.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/volvelle/canvas/p1"
                },
                {
                  "id": "https://example.org/iiif/volvelle/annotation/disc1",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/volvelle/rotating-disc.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 800,
                    "width": 800
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/volvelle/canvas/p1",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=600,1100,800,800"
                    }
                  },
                  "body": {
                    "type": "Choice",
                    "items": [
                      {
                        "id": "https://example.org/iiif/volvelle/disc-rotation-0.png",
                        "type": "Image",
                        "label": { "en": [ "0 degrees" ] }
                      },
                      {
                        "id": "https://example.org/iiif/volvelle/disc-rotation-90.png",
                        "type": "Image",
                        "label": { "en": [ "90 degrees" ] }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }
      ]
    }
---

## Additional Context

Volvelles represent one of the earliest forms of interactive information display, predating modern computing by centuries. They combine aesthetic beauty with functional purpose, making them fascinating objects for digital preservation and interaction.

### Implementation Notes

When implementing digital volvelles, consider:

- **Rotation Mechanics**: Allow smooth rotation of the disc layer(s) either through click-and-drag or by clicking specific positions
- **Layering**: Properly handle z-index to ensure rotating elements appear above the base page but below any fixed pointer elements
- **Transparency**: Support transparent or cut-out regions in the rotating disc that reveal information from layers below
- **Multiple Discs**: Some volvelles have multiple independently rotating discs
- **Alignment Markers**: Include visual indicators to show when specific positions or combinations are aligned
- **Historical Context**: Provide information about the original purpose and usage of the volvelle

### Technical Considerations

The IIIF Presentation API can represent volvelles using:
- Multiple annotation layers for different rotating elements
- Choice bodies to show different rotational states
- Fragment selectors to position rotating elements precisely
- Web Annotations to describe the rotational behavior and interaction points
