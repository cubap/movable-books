---
layout: use_case
title: "Fold"
description: |
  A fold represents one or more connected parts of a page that can move independently around a hinge or crease. This includes various types of folded elements such as fold-out maps, gatefolds, accordion folds, and pop-up mechanisms where panels are connected but can be positioned at different angles or configurations.
  
  The key characteristic is that multiple parts remain physically connected along a fold line (hinge) but can be positioned independently, revealing different content or creating three-dimensional structures.
examples: |
  Common examples include:
  
  - **Fold-out Maps**: A large map folded to fit within a book that unfolds to reveal the full extent of the geographical area
  - **Gatefolds**: Two panels that fold out from the center, often used for panoramic images or large diagrams
  - **Accordion Folds**: Multiple panels connected in a zigzag pattern, commonly used in Asian handscrolls or modern artist books
  - **Pop-up Elements**: Folded paper structures that create three-dimensional forms when the page is opened
instances:
  - title: "Blaeu Atlas Fold-out Map"
    url: "#"
    description: "17th-century atlas with large fold-out maps of continents"
  - title: "Pop-up Book Page"
    url: "#"
    description: "Victorian pop-up book with architectural scenes that rise when opened"
  - title: "Japanese Accordion Book (Orihon)"
    url: "#"
    description: "Traditional Japanese book format with continuous zigzag folding"
links:
  - title: "Book Structures and Formats"
    url: "https://www.nedcc.org/free-resources/preservation-leaflets/4.-storage-and-handling/4.10-storage-methods-and-handling-practices"
data:
  manifest: |
    {
      "@context": "http://iiif.io/api/presentation/3/context.json",
      "id": "https://example.org/iiif/fold/manifest",
      "type": "Manifest",
      "label": { "en": [ "Fold Example - Gatefold" ] },
      "items": [
        {
          "id": "https://example.org/iiif/fold/canvas/base",
          "type": "Canvas",
          "label": { "en": [ "Base Page" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/fold/page/base/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/fold/annotation/base",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/fold/base.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/fold/canvas/base"
                }
              ]
            }
          ]
        },
        {
          "id": "https://example.org/iiif/fold/canvas/left-panel",
          "type": "Canvas",
          "label": { "en": [ "Left Fold-out Panel" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/fold/page/left/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/fold/annotation/left",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/fold/left-panel.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/fold/canvas/left-panel"
                }
              ]
            }
          ]
        },
        {
          "id": "https://example.org/iiif/fold/canvas/right-panel",
          "type": "Canvas",
          "label": { "en": [ "Right Fold-out Panel" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/fold/page/right/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/fold/annotation/right",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/fold/right-panel.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/fold/canvas/right-panel"
                }
              ]
            }
          ]
        }
      ]
    }
---

## Additional Context

Folds in books serve both practical and aesthetic purposes. Practically, they allow large images or documents to fit within the bound format. Aesthetically, they create moments of revelation and surprise as the reader unfolds hidden content.

### Implementation Notes

When implementing digital representations of folds:

- **Fold States**: Represent multiple states (fully folded, partially unfolded, fully unfolded)
- **Hinge Visualization**: Show the connection point between folded elements
- **Sequence**: Define the order in which panels should be unfolded
- **Viewing Options**: Offer both animated unfolding and direct access to different states
- **Composite Views**: Provide a way to see all panels aligned as they would appear when fully extended
- **3D Representation**: For pop-ups, consider using 3D models or perspective views to show the raised elements

### Viewing Considerations

Different fold types require different viewing approaches:

- **Single Fold-out**: Show folded state, transition animation, and unfolded state
- **Gatefolds**: Allow progressive unfolding from center outward
- **Accordion Folds**: Enable sequential navigation through connected panels
- **Pop-ups**: Provide multiple angle views or interactive 3D models to show depth
