async function fetchLinkPreview(url) {
  try {
    const response = await fetch(url);
    const html = await response.text();

    // Extract title and meta tags from the HTML
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    const title = doc.querySelector('title').textContent;
    const description = doc.querySelector('meta[name="description"]').getAttribute('content');
    const image = doc.querySelector('meta[property="og:image"]').getAttribute('content');

    // Display the preview elements
    document.getElementById('preview-title').textContent = title;
    document.getElementById('preview-description').textContent = description;
    document.getElementById('preview-image').src = image;
  } catch (error) {
    console.error('Error fetching preview:', error);
    // Handle errors, e.g., display an error message
  }
}
