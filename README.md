# Bspoke-cases
This Repo is dedicated to showcase my solutions and thought process for multiple cases.


# Case 1
Update the website's HTML, without using JavaScript or CSS, to make use of semantic elements so that: 
- The classless outer div element is replaced with a more appropriate element.
- The divs with the image and caption classes are replaced with self-contained content elements.
- The divs with the lorem-ipsum and description classes are replaced with elements, so that by default only the contents of the description element are shown.
- When the contents of the description element are clicked, the visibility of the rest of the lorem-ipsum element is toggled.

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

!!  TODO !! ADD GIF

```
## Solution
Not being quite familiar with sematic elements in HTML made this case quite a challenge. I felt that i had quite a good understanding after reading up about them and i quickly understood that they helped the developer understand what role the element played in the document, instead of the dreaded chain of divs with a multitude of confusing classes. 

However, I didn't know that these elements had functionalities. Thats why the words "without using JavaScript or CSS" stumped me. I thought it was a typo at first, thinking it was impossible to toggle the visibility of content in HTML without them. But after seeing that the ```<figure>``` element had an actual effect on the contents inside, i knew that these elements had built in functionalities. After looking around some more, I came across a YouTube video leading to [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) resource, conveniently listing all HTML elements and their functions. 

Using ```Ctrl + F``` and searching for "Details" i found the ```<details>``` and ```<summary>``` duo, who's description perfectly matched my usecase. Here i also found descriptions for the ```<main>``` and ```<article>``` elements which i also used in my answer, whos descriptions deepend my knowlege about them. This assignment has opened my eyes to more functionalities within HTML itself, and i will continue using them in projects to learn more about them. All this lead to my answer:
```HTML
<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
<title>Semantics</title>
</head>

<body>
    <main>
        <h1>Lorem Ipsum</h1>

    <figure>
        <img src="https://bit.ly/3ftgXAt" alt="Lorem Ipsum">
        <figcaption>Lorem Ipsum</figcaption>
    </figure>

    <article>
        <details>
        <summary>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</summary>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Curabitur vitae hendrerit mauris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Mauris lacinia scelerisque nibh nec gravida. 
        Duis malesuada nec nibh sit amet pulvinar. 
        Phasellus congue porttitor arcu, ut suscipit nibh aliquam vel. 
        Nunc arcu lectus, egestas ut sem ac, euismod porttitor eros. 
        Phasellus tincidunt consequat pharetra. Maecenas sodales purus at nulla finibus dapibus. 
        Nullam varius at nisl vel euismod. Fusce aliquet ligula non tempor fermentum. 
        Nam fermentum posuere mauris, quis aliquam nibh dictum sed.
        </details>  
    </article>

  </main>
</body>
</html>
```

# Case 2
Write a function that removes all items that are not numbers from the array. The function should modify the existing array, not create a new one.
For example, if the input array contains values ``[1, 'a', 'b', 2]``, after processing, the array will contain only values ``[1, 2]``.

Example:

```javascript
function filterNumbersFromArray(arr) {
  // Write the code that goes here
}
var arr = [1, 'a', 'b', 2];
filterNumbersFromArray(arr);
// At this point, arr should have been modified in place
// and contain only 1 and 2.
for (var i = 0; i < arr.length; i++)
  console.log(arr[i]);
 ```
## Solution
In the beginning i thought i could just loop though the Array and use the ```splice``` function to remove items from the Array by modifying the Array itself. 
```JS
function filterNumbersFromArray(arr) {
  arr.forEach((item) => {
    if (typeof item == 'string'){
      arr.splice(arr.indexOf(item), 1)
    }
  })
}
```
Nevertheless, this did not work due to the length of the Array changing as the loop checked the items of it making the loop skip some items.
<img src='https://user-images.githubusercontent.com/106773288/225982042-8b61db22-5012-4344-bd1d-3a6ef4e4f1c8.png' width='50%'>
<br>
<img src='https://user-images.githubusercontent.com/106773288/225982246-f8e7b9b9-51a6-4988-8a83-6c47a0b3ad70.png' width='50%'>
<br>
<img src='https://user-images.githubusercontent.com/106773288/225982473-0637def2-d798-4369-b4f0-bc779517f5a5.png' width='50%'>
<br>The function notices that the value is a string and removes it. However, it does not notice that the item at the same index in the newly modified Array is a string before it increments onto the next element. Thereby skipping a string.<br>
<img src='https://user-images.githubusercontent.com/106773288/225982578-3045bb1f-9ba3-4c8a-ae6f-1d2fdbfecd0f.png' width='50%'>

This lead to my final solution:
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
        function filterNumbersFromArray(arr) {
            for (let i = 0; i < arr.length; i++){
                let item = arr[i]
                if (typeof item == "string"){
                    arr.splice(i, 1)
                    i -= 1 // Compensate for Array length change when using arr.splice()
                }
            }
        }

        var arr = [1, 'a', 'b', 2]

        filterNumbersFromArray(arr)
        // At this point, arr should have been modified in place
        // and contain only 1 and 2.
        for (var i = 0; i < arr.length; i++){
            console.log(arr[i]) // -> [1, 2]
        }
    </script>
</body>
</html>
```
By simply reducing ``i`` after removing an item from the Array we compensate for the length reduction of the Array and the function works correctly.


https://github.com/Acaippa/Bspoke-cases/blob/main/code/Answer%20%232.html#:~:text=lines%20(27%20sloc,%3C/html%3E
