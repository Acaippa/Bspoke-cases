# Bspoke-cases
This Repo is dedicated to showcase my solutions and thought process for multiple cases.


# Case 1
Update the website's HTML, without using JavaScript or CSS, to make use of semantic elements so that: 
- The classless outer div element is replaced with a more appropriate element.
- The divs with the image and caption classes are replaced with self-contained content elements.
- The divs with the lorem-ipsum and description classes are replaced with elements, so that by default only the contents of the description element are shown.
- When the contents of the description element are clicked, the visibility of the rest of the lorem-ipsum element is toggled.
- 
Example:
```HTML
<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
<title>Semantics</title>
</head>

<body>
  <div>
    <h1>Lorem Ipsum</h1>
    <div class="image">
      <img src="https://bit.ly/3ftgXAt" alt="Lorem Ipsum">
      <div class="caption">Lorem Ipsum</div>
    </div>
    <div class="lorem-ipsum">
      <div class="description">Lorem ipsum dolor sit amet, consectetur adipiscing elit...</div>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
      Curabitur vitae hendrerit mauris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
      Mauris lacinia scelerisque nibh nec gravida. 
      Duis malesuada nec nibh sit amet pulvinar. 
      Phasellus congue porttitor arcu, ut suscipit nibh aliquam vel. 
      Nunc arcu lectus, egestas ut sem ac, euismod porttitor eros. 
      Phasellus tincidunt consequat pharetra. Maecenas sodales purus at nulla finibus dapibus. 
      Nullam varius at nisl vel euismod. Fusce aliquet ligula non tempor fermentum. 
      Nam fermentum posuere mauris, quis aliquam nibh dictum sed.</p>
    </div>
  </div>
</body>
</html>
```
