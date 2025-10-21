---
layout: use_case
title: "Slider"
description: |
  A slider is a movable part of a document that follows a defined path between two or more anchor points, typically moving in a straight line without flipping to reveal a new face. Sliders create dynamic interactions by revealing hidden content, changing visible combinations, or providing tactile engagement with the document.
  
  The key characteristic is that the slider element moves along a constrained path (usually a slot or track) while maintaining the same face visible to the viewer, unlike pages that turn or volvelles that rotate around a central point.
examples: |
  Common examples include:
  
  - **Pull-tab Books**: Children's books where pulling a tab causes elements to move across the page, such as animals moving through a scene or vehicles traveling along a road
  - **Reveal Mechanisms**: Sliders that move to expose hidden text or images beneath a covering layer, often used for answers to questions or surprise elements
  - **Transformation Scenes**: Moving elements that change a scene, such as day-to-night transitions or before-and-after comparisons
  - **Educational Diagrams**: Anatomical or mechanical illustrations where sliding parts demonstrate movement, stages of development, or internal structures
  - **Interactive Calendars**: Movable date indicators that slide along a track to mark the current day or month
instances:
  - title: "Victorian Mechanical Book"
    url: "#"
    description: "19th-century novelty book with sliding panels revealing hidden images"
  - title: "Anatomy Slider Book"
    url: "#"
    description: "Medical education book with sliding layers showing different body systems"
  - title: "Pull-the-Tab Storybook"
    url: "#"
    description: "Modern children's book where pulling tabs animates characters and objects"
links:
  - title: "Movable Books Society"
    url: "http://www.movablebooksociety.org/"
  - title: "Pop-up and Movable Books: A Bibliography"
    url: "https://popartmachine.com/pages/pop-up-movable-books"
data:
  manifest: |
    {
      "@context": "http://iiif.io/api/presentation/3/context.json",
      "id": "https://example.org/iiif/slider/manifest",
      "type": "Manifest",
      "label": { "en": [ "Slider Example - Pull-tab Reveal" ] },
      "items": [
        {
          "id": "https://example.org/iiif/slider/canvas/page",
          "type": "Canvas",
          "label": { "en": [ "Interactive Page with Slider" ] },
          "height": 3000,
          "width": 2000,
          "items": [
            {
              "id": "https://example.org/iiif/slider/page/base/1",
              "type": "AnnotationPage",
              "items": [
                {
                  "id": "https://example.org/iiif/slider/annotation/background",
                  "type": "Annotation",
                  "motivation": "painting",
                  "body": {
                    "id": "https://example.org/iiif/slider/background.jpg",
                    "type": "Image",
                    "format": "image/jpeg",
                    "height": 3000,
                    "width": 2000
                  },
                  "target": "https://example.org/iiif/slider/canvas/page"
                },
                {
                  "id": "https://example.org/iiif/slider/annotation/slider-position-1",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Slider - Start Position" ] },
                  "body": {
                    "id": "https://example.org/iiif/slider/slider-element.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 600,
                    "width": 800
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/slider/canvas/page",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=100,1200,800,600"
                    }
                  }
                },
                {
                  "id": "https://example.org/iiif/slider/annotation/slider-position-2",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Slider - Mid Position" ] },
                  "body": {
                    "id": "https://example.org/iiif/slider/slider-element.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 600,
                    "width": 800
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/slider/canvas/page",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=600,1200,800,600"
                    }
                  }
                },
                {
                  "id": "https://example.org/iiif/slider/annotation/slider-position-3",
                  "type": "Annotation",
                  "motivation": "painting",
                  "label": { "en": [ "Slider - End Position" ] },
                  "body": {
                    "id": "https://example.org/iiif/slider/slider-element.png",
                    "type": "Image",
                    "format": "image/png",
                    "height": 600,
                    "width": 800
                  },
                  "target": {
                    "type": "SpecificResource",
                    "source": "https://example.org/iiif/slider/canvas/page",
                    "selector": {
                      "type": "FragmentSelector",
                      "value": "xywh=1100,1200,800,600"
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

Sliders represent a sophisticated form of mechanical book design that emerged prominently in the 19th century with the rise of movable books for children and educational purposes. Unlike other movable elements, sliders create the illusion of continuous motion along a defined trajectory.

### Implementation Notes

When implementing digital representations of sliders:

- **Path Definition**: Clearly define the start and end points of the slider's path
- **Intermediate States**: Capture multiple positions along the slider's path to show the full range of motion
- **Animation**: Consider smooth animation between states when the user interacts with the slider
- **Track Visualization**: Optionally show the path or slot that constrains the slider's movement
- **Pull Tab**: Represent the visible tab or handle that would be used to move the slider
- **Hidden Content**: Show what is revealed or concealed as the slider moves
- **Directional Constraints**: Ensure the slider only moves along its intended axis
- **Snap Points**: Define specific positions where the slider naturally rests

### Viewing Considerations

Different slider types require different viewing approaches:

- **Linear Reveals**: Show before, during, and after states of content being revealed
- **Scene Changes**: Provide smooth transitions between different scene configurations
- **Cyclical Sliders**: For sliders that can move in a continuous loop, enable repeated motion
- **Multiple Sliders**: When a page has several independent sliders, allow them to be manipulated separately
- **Linked Movement**: Some sliders cause multiple elements to move simultaneously; represent these relationships

### Technical Considerations

The IIIF Presentation API can represent sliders using:
- Multiple annotations with fragment selectors showing different positions
- Choice bodies or supplementing annotations for different slider states
- Temporal annotations to sequence the movement
- Web Annotations to describe the slider mechanism, path constraints, and interaction points

### Preservation Considerations

When digitizing slider materials:

- Document the full range of motion from start to end
- Capture any damage or wear to the slider mechanism
- Photograph the reverse side to show the mechanical structure
- Record whether the slider still moves freely or is stuck
- Note any missing parts or broken tabs
- Document the intended direction and extent of movement
