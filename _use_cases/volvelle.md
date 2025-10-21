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
  - title: "Insert great examples here!"
    url: "#nothing"
    description: "16th-century astronomical computing device with rotating paper discs"
links:
  - title: "Wikipedia: Volvelle"
    url: "https://en.wikipedia.org/wiki/Volvelle"
data:
  manifest: "https://cubap.github.io/movable-books/fixtures/manifests/all.json"
---

## Implementation Notes

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
