---
layout: use_case
title: "Perspective"
description: |
  A perspective document is one intended to be configured and viewed from a specific point or through a fixed perspective window. These documents use principles of linear perspective, anamorphosis, or optical illusion to create images that only appear correct when viewed from a particular angle, distance, or through a specialized viewing device.
  
  The key characteristic is that the document's full meaning or visual coherence is only achieved under specific viewing conditions, often creating dramatic reveals or surprising transformations when viewed correctly versus incorrectly.
examples: |
  Common examples include:
  
  - **Anamorphic Art**: Images that appear distorted or unrecognizable when viewed directly but resolve into recognizable forms when viewed from an extreme angle or reflected in a cylindrical or conical mirror
  - **Peep Shows (Perspective Boxes)**: Layered scenes viewed through a small aperture that create the illusion of three-dimensional depth through forced perspective
  - **Tunnel Books**: Accordion-like books with cutout scenes that create depth when viewed through an opening at one end
  - **Perspective Theaters**: Printed theatrical scenes with multiple layers that create stage-like depth when properly assembled and viewed
  - **Lenticular Prints**: Images that change or move when viewed from different angles due to lenticular lensing technology
instances:
  - title: "Holbein's The Ambassadors (Anamorphic Skull)"
    url: "https://www.nationalgallery.org.uk/paintings/hans-holbein-the-younger-the-ambassadors"
    description: "Famous painting with anamorphic skull visible only from specific viewing angle"
  - title: "18th-century Peep Show Box"
    url: "#"
    description: "Dutch perspective box creating illusion of deep interior space"
  - title: "Victorian Tunnel Book"
    url: "#"
    description: "Layered paper theater scene with remarkable depth effect"
links:
  - title: "Anamorphic Art"
    url: "https://en.wikipedia.org/wiki/Anamorphosis"
  - title: "Tunnel Books"
    url: "https://www.vam.ac.uk/articles/an-introduction-to-tunnel-books"
data:
  manifest: |
    {
      "@context": "http://iiif.io/api/presentation/3/context.json",
      "id": "https://example.org/iiif/perspective/manifest",
      "type": "Manifest",
      "label": { "en": [ "Perspective Example - Tunnel Book" ] },
      "items": [
        {
          "id": "https://example.org/iiif/perspective/canvas/view-direct",
          "type": "Canvas",
          "label": { "en": [ "Direct View (Collapsed)" ] },
          "height": 2000,
          "width": 3000,
          "items": [
            {
              "id": "https://example.org/iiif/perspective/page/direct/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/perspective/annotation/collapsed",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/perspective/collapsed-view.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 2000,
                    "width": 3000
                  },
                  "target": "https://example.org/iiif/perspective/canvas/view-direct"
                }
              ]
            }
          ]
        },
        {
          "id": "https://example.org/iiif/perspective/canvas/view-perspective",
          "type": "Canvas",
          "label": { "en": [ "Perspective View (Through Opening)" ] },
          "height": 2000,
          "width": 3000,
          "items": [
            {
              "id": "https://example.org/iiif/perspective/page/perspective/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/perspective/annotation/layer-1",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Foreground Layer" ] },
                  "body": {
                    "id": "https://example.org/iiif/perspective/layer-1-foreground.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 2000,
                    "width": 3000
                  },
                  "target": "https://example.org/iiif/perspective/canvas/view-perspective"
                },
                {
                  "id": "https://example.org/iiif/perspective/annotation/layer-2",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Mid Layer 1" ] },
                  "body": {
                    "id": "https://example.org/iiif/perspective/layer-2-mid.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 1800,
                    "width": 2700
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/perspective/canvas/view-perspective",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=150,100,2700,1800"
                    }
                  }
                },
                {
                  "id": "https://example.org/iiif/perspective/annotation/layer-3",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Mid Layer 2" ] },
                  "body": {
                    "id": "https://example.org/iiif/perspective/layer-3-mid.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 1600,
                    "width": 2400
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/perspective/canvas/view-perspective",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=300,200,2400,1600"
                    }
                  }
                },
                {
                  "id": "https://example.org/iiif/perspective/annotation/layer-4",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Background Layer" ] },
                  "body": {
                    "id": "https://example.org/iiif/perspective/layer-4-background.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 1400,
                    "width": 2100
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/perspective/canvas/view-perspective",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=450,300,2100,1400"
                    }
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

Perspective-based documents represent a sophisticated intersection of art, optics, and book design. From Renaissance experiments with anamorphic art to Victorian peep shows and tunnel books, these objects have long fascinated viewers with their ability to transform depending on the viewing angle or method.

### Implementation Notes

When implementing digital representations of perspective documents:

- **Multiple Views**: Provide both the "incorrect" (direct) view and the "correct" (intended perspective) view
- **Viewing Instructions**: Clearly explain how the document should be viewed to achieve the intended effect
- **Layer Separation**: For tunnel books and similar objects, show individual layers separately as well as the composite view
- **3D Visualization**: Consider providing a 3D model or animation showing the spatial arrangement of layers
- **Viewing Angle Indicator**: Show or describe the optimal viewing angle for anamorphic images
- **Reflection Simulation**: For cylindrical or conical mirror anamorphoses, simulate the corrected view
- **Interactive Exploration**: Allow users to change viewing angle or distance to see the transformation
- **Depth Simulation**: Use parallax effects or 3D rendering to simulate the depth effect of layered scenes

### Viewing Considerations

Different perspective types require different viewing approaches:

- **Anamorphic Images**: Show both the distorted original and a corrected/reflected view
- **Tunnel Books**: Provide views of individual layers, the assembled structure, and the view through the front opening
- **Peep Shows**: Simulate the view through the peephole while also showing the full construction
- **Perspective Theaters**: Display the flat collapsed state and the erected three-dimensional viewing state
- **Lenticular Prints**: Animate between the different images visible at different angles

### Technical Considerations

The IIIF Presentation API can represent perspective documents using:
- Multiple canvases for different viewing states or angles
- Layered annotations with precise positioning to simulate depth
- 3D viewing hints or custom rendering instructions
- Annotations describing viewing requirements and optimal positions
- Choice bodies to switch between viewing modes

### Preservation Considerations

When digitizing perspective documents:

- Capture both the assembled and disassembled states
- Photograph from the intended viewing angle/position
- Document the viewing mechanism (mirrors, lenses, apertures)
- Capture individual layers separately before and after assembly
- Record the spatial relationships between layers
- Measure depths, angles, and distances critical to the effect
- Photograph the construction method and materials
- Test and document whether the perspective effect still works
- Note any damage to layers or viewing mechanisms
