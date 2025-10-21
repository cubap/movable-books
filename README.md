# movable-books
Collecting use cases and generating fixtures for movable books in IIIF

## About

This Jekyll-based website documents use cases for representing interactive and movable elements in digitized books using the IIIF (International Image Interoperability Framework) standards.

## Structure

- **`_layouts/`** - Jekyll layout templates
  - `default.html` - Base layout with header and footer
  - `post.html` - Layout for blog posts with edit links
  - `use_case.html` - Structured layout for use case documentation
- **`_use_cases/`** - Use case documentation files
- **`_posts/`** - Blog posts and announcements
- **`assets/css/`** - Stylesheets (IIIF-inspired design)
- **`index.html`** - Homepage

## Use Case Structure

Each use case page includes the following sections:

- **Description** - Basic explanation of the use case
- **Examples** - Generic but specific examples with space for images, videos, or text
- **Instances** - Real Internet resources that embody this example
- **Data** - Sample IIIF Manifest or Canvas data
- **Links** - Relevant resources (IIIF Slack, GitHub, etc.)

## Contributing

All pages include an "Edit this page" link that takes you to GitHub where you can propose changes. You can:

- Add new use cases
- Improve existing documentation
- Add examples and instances
- Provide feedback on data structures

## Local Development

1. Install Ruby and Bundler
2. Install dependencies:
   ```bash
   bundle install
   ```
3. Run Jekyll locally:
   ```bash
   bundle exec jekyll serve
   ```
4. Visit `http://localhost:4000`

## Resources

- [IIIF Community Group on Slack](https://iiif.slack.com/archives/C093P3XRLK1)
- [IIIF Website](https://iiif.io)
- [Use Cases Discussion (Issue #1)](https://github.com/cubap/movable-books/issues/1)
