---
layout: use_case
title: "Cutout"
description: |
  A cutout is a removable or detachable part of a document intended to be used atop the main document or as a separate piece. These elements are typically printed on the same page as the main content but designed to be cut out and used independently, often for educational, entertainment, or interactive purposes.
  
  The key characteristic is that the cutout piece is separable from its original context and can be positioned over different parts of the document or used entirely independently, creating new combinations or interactions.
examples: |
  Common examples include:
  
  - **Paper Dolls**: Figures and clothing items printed on a page that can be cut out and dressed by overlaying garments on the doll
  - **Model Templates**: Architectural or mechanical models printed flat that can be cut out and assembled into three-dimensional structures
  - **Interactive Overlays**: Transparent or semi-transparent cutouts that reveal answers, decode messages, or highlight specific information when placed over the base document
  - **Game Pieces**: Playing pieces, cards, or tokens that are cut from a printed sheet to be used in board games or educational activities
  - **Masks and Costumes**: Wearable items like masks or crowns that are printed as part of a book but intended to be removed and worn
instances:
  - title: "Victorian Paper Doll Collection"
    url: "#"
    description: "19th-century children's book with elaborately illustrated paper dolls and costumes"
  - title: "Pop-out Model Cathedral"
    url: "#"
    description: "Architectural model of Notre-Dame that can be assembled from printed cutouts"
  - title: "Decoder Wheel Activity Book"
    url: "#"
    description: "Educational book with transparent overlay discs for revealing hidden messages"
links:
  - title: "Paper Dolls History"
    url: "https://en.wikipedia.org/wiki/Paper_doll"
  - title: "Pop-up and Movable Books"
    url: "https://www.popuplady.com/"
data:
  manifest: |
    {
      "@context": "http://iiif.io/api/presentation/3/context.json",
      "id": "https://example.org/iiif/cutout/manifest",
      "type": "Manifest",
      "label": { "en": [ "Cutout Example - Paper Doll" ] },
      "items": [
        {
          "id": "https://example.org/iiif/cutout/canvas/base",
          "type": "Canvas",
          "label": { "en": [ "Base Page" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/cutout/page/base/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/cutout/annotation/base",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/cutout/base-page.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/cutout/canvas/base"
                }
              ]
            }
          ]
        },
        {
          "id": "https://example.org/iiif/cutout/canvas/doll",
          "type": "Canvas",
          "label": { "en": [ "Paper Doll Cutout" ] },
          "height": 1200,
          "width": 400,
          "items": [
            {
              "id": "https://example.org/iiif/cutout/page/doll/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/cutout/annotation/doll",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/cutout/doll.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 1200,
                    "width": 400
                  },
                  "target": "https://example.org/iiif/cutout/canvas/doll"
                }
              ]
            }
          ]
        },
        {
          "id": "https://example.org/iiif/cutout/canvas/outfit1",
          "type": "Canvas",
          "label": { "en": [ "Outfit 1 Cutout" ] },
          "height": 800,
          "width": 600,
          "items": [
            {
              "id": "https://example.org/iiif/cutout/page/outfit1/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/cutout/annotation/outfit1",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/cutout/outfit1.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 800,
                    "width": 600
                  },
                  "target": "https://example.org/iiif/cutout/canvas/outfit1"
                }
              ]
            }
          ]
        }
      ]
    }
---

## Additional Context

Cutouts represent one of the oldest forms of interactive printed materials, dating back to at least the 18th century with the popularity of paper dolls and educational movable books. They bridge the gap between passive reading and active play, transforming a static document into an interactive experience.

### Implementation Notes

When implementing digital representations of cutouts:

- **Separate Canvases**: Represent each cutout element as a separate canvas to allow independent manipulation
- **Positioning**: Allow users to drag and position cutout elements over the base document or other surfaces
- **Layering**: Maintain proper z-index so cutouts appear above the base page when positioned
- **Original Context**: Provide a view showing the cutouts in their original printed position (uncut state)
- **Cut Lines**: Include visual indicators of where cuts should be made in the original document
- **Assembly Instructions**: For complex cutouts like models, include step-by-step assembly guidance
- **Transparency**: Support PNG or other formats with transparency for cutouts that aren't rectangular

### Viewing Considerations

Different cutout types require different viewing approaches:

- **Paper Dolls**: Provide a workspace where dolls and clothing can be mixed and matched
- **Model Templates**: Show both flat (printable) and assembled (3D preview) states
- **Decoder Overlays**: Allow precise alignment with specific positions on the base document
- **Game Pieces**: Enable organization into sets or categories for gameplay
- **Educational Cutouts**: Provide context about the learning objectives and suggested activities

### Preservation Considerations

When digitizing cutout materials:

- Document both cut and uncut states when possible
- Capture all elements, even if already separated from the original sheet
- Record any assembly marks, fold lines, or instructions
- Photograph assembled models from multiple angles
- Note the condition and whether pieces are missing or damaged
