---
layout: use_case
title: "Fold"
description: |
  A fold represents one or more connected parts of a page that can move independently around a hinge or crease. This includes various types of folded elements such as fold-out maps, gatefolds, accordion folds, and pop-up mechanisms where panels are connected but can be positioned at different angles or configurations.
  
  The key characteristic is that multiple parts remain physically connected along a fold line (hinge) but can be positioned independently, revealing different content or creating three-dimensional structures.
examples: |
  Common examples include:
  
  - **Flaps**: Small folded sections that can be lifted to reveal hidden content underneath
  - **Accordion Folds**: Multiple panels connected in a zigzag pattern, commonly used in Asian handscrolls or modern artist books
  - **Fold-out Maps**: A large map folded to fit within a book that unfolds to reveal the full extent of the geographical area
  - **Gatefolds**: Two panels that fold out from the center, often used for panoramic images or large diagrams
  - **Pop-up Elements**: Folded paper structures that create three-dimensional forms when the page is opened
instances:
  - title: "Please edit some examples here!"
    url: "#nothing"
    description: "17th-century atlas with large fold-out maps of continents"

links:
  - title: "Book Structures and Formats"
    url: "https://www.nedcc.org/free-resources/preservation-leaflets/4.-storage-and-handling/4.10-storage-methods-and-handling-practices"
data:
  manifest: "https://cubap.github.io/movable-books/fixtures/manifests/all.json"
---

## Implementation Notes

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
