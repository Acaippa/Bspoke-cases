# Bspoke cases
The following content displays several assignments, as well as their answers. 
Contents

- [Assignment 1](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-1)
- [Assignment 2](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-2)
- [Assignment 3](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-3)
- [Assignment 4](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-4)
- [Assignment 5](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-5)
- [Assignment 6](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-6)
- [Assignment 7](https://github.com/Acaippa/Bspoke-cases/edit/main/README.md#assignment-7)

# Assignment 1
Update the website's HTML, without using JavaScript or CSS, to make use of semantic elements so that: 
- The classless outer div element is replaced with a more appropriate element.
- The divs with the image and caption classes are replaced with self-contained content elements.
- The divs with the lorem-ipsum and description classes are replaced with elements, so that by default only the contents of the description element are shown.
- When the contents of the description element are clicked, the visibility of the rest of the lorem-ipsum element is toggled.

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
## Solution
Not being quite familiar with sematic elements in HTML made this assignment quite a challenge. I felt that I had quite a good understanding after reading up about them and i quickly understood that they helped the developer understand what role the element played in the document, instead of the dreaded chain of divs with a multitude of confusing classes. 

However, I didn't know that these elements had functionalities. That’s why the words "without using JavaScript or CSS" stumped me. I thought it was a typo at first, thinking it was impossible to toggle the visibility of content in HTML without them. But after seeing that the ```<figure>``` element had an actual effect on the contents inside, i knew that these elements had built in functionalities. After looking around some more, I came across a YouTube video leading to [this](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) resource, conveniently listing all HTML elements and their functions. 

Using ```Ctrl + F``` and searching for "Details" i found the ```<details>``` and ```<summary>``` duo, who's description perfectly matched my usecase. Here i also found descriptions for the ```<main>``` and ```<article>``` elements which i also used in my answer, whos descriptions deepend my knowlege about them. This assignment has opened my eyes to more functionalities within HTML itself, and i will continue using them in projects to learn more about them. All this led to my answer:
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

![case 1 gif](https://user-images.githubusercontent.com/106773288/226929272-cb735afe-633d-425d-a88f-cd963fcbf8be.gif)


# Assignment 2
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
In the beginning I thought I could just loop though the Array and use the ```splice``` function to remove items from the Array by modifying the Array itself. 
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

# Assignment 3
This web page displays a list of baby names.
At the moment it does not use space efficiently.
Write CSS so that the baby-names is a Flexbox and configure it's properties so that the items are displayed vertically.
They should wrap and be centered both horizontally.

Example:
```HTML
<!DOCTYPE html>
<html>
    <head>
    <title>Baby Names</title>
    <style>
    /* Insert your CSS solution here */ 
    </style>
    </head>
 <body>
    <div id="baby-names">
      <p>Stacy</p>
      <p>John</p>
      <p>Peter</p>
   </div>
  </body>
</html>
 ```
 
 ![case 3 gif](https://user-images.githubusercontent.com/106773288/226929944-82163d29-ad4e-425d-94e5-1791ffecbce0.gif)

 
## Solution
I wasn’t sure as to how to solve this one. After selecting ```#baby-names``` and after setting the ```display``` and ```direction``` to ```flex``` and ```column```, i felt stuck. So after looking around, i found [This](https://stackoverflow.com/questions/45442906/get-divs-to-wrap-horizontally#:~:text=ul%20%7B%0A%20%20display%3A%20flex%3B%0A%20%20height%3A%20100vh%3B%0A%20%20flex%2Ddirection%3A%20column%3B%0A%20%20align%2Ditems%3A%20flex%2Dstart%3B%0A%20%20align%2Dcontent%3A%20flex%2Dstart%3B%0A%20%20flex%2Dwrap%3A%20wrap%3B%0A%20%20list%2Dstyle%3A%20none%3B%0A%20%20padding%3A%200%3B%0A%7D) article showing that I was quite close, but I was missing a static height of ```100vh``` and ```flex-wrap: wrap;``` as well as changing ```align-items``` and removing ```align-content``` to allow for centered items. Leading to my solution:
```HTML
<!DOCTYPE html>
<html>
    <head>
    <title>Baby Names</title>
    <style>
        #baby-names {
            display: flex;
            flex-direction: column;
            height: 100vh;
            flex-wrap: wrap;
            align-items: center;
        }
    </style>
    </head>
 <body>
    <div id="baby-names">
      <p>Stacy</p>
      <p>John</p>
      <p>Peter</p>
   </div>
  </body>
</html>
```
# Assignment 4
Which of the following statements are true for merging feature and master branches? (Select all acceptable answers.)

- [x] GIT ensures that conflicts never happen.

  Whenever Git detects a conflict, it will try its best to work it out. However, at times the developer will need to change their code to avoid the conflict. [Source](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts#:~:text=Conflicts%20generally%20arise,resolve%20the%20conflict.)
  <hr>
- [x] A push command to the master branch can fail if the master branch was modified in the meantime.

  If the push command conflicts with the modification, Git will prevent the push.
  <hr>
- [x] After merging, git-blame will list only one developer for every modified source code file.

  According to [this](https://stackoverflow.com/questions/15769298/git-blame-correct-author-after-merge#:~:text=This%20causes%20problems%20with%20%22git%20blame%22%3A%20the%20merged%20lines%20appear%20to%20be%20committed%20by%20the%20developer%20that%20did%20the%20merge) Git-blame will show that the code was made by the developer who committed the merge.
  <hr>
- [x] Before merging, we can sync changes from the master branch to the feature branch.

  By checking out the master branch and merging it to the feature branch, before merging the feature branch back into the master branch we can sync the feature branch. [Source](https://stackoverflow.com/questions/16329776/how-to-keep-a-branch-synchronized-updated-with-master#:~:text=Yes%2C%20just%20do,a%20good%20place.)
  <hr>
- [x] Each developer can have their own local branches and commit changes to them. These branches are not visible to other developers until the developer publishes the changes.

  By forking any public repository, you can locally make any changes you like to it before sending a pull request to the original repository, asking them to implement your code to the actual product. [Source](https://www.freecodecamp.org/news/how-to-fork-a-github-repository/#:~:text=so%20you%20can%20make,to%20review%20your%20changes.)

  <hr>
- [ ] The feature branch cannot be branched further.

  I was pretty sure this was possible. Nevertheless, I wanted to try it in practice using Sublime merge for a more visual representation. It works, however I think it looks a bit complicated and scary.

  ![image](https://user-images.githubusercontent.com/106773288/226183641-9611bd16-8651-4743-9ab5-39b2cd774def.png)

# Assignment 5
Complete the function generateNewFolderName that receives an array of folder names and returns a generated unique folder name using the following rules:

If there is no folder with the name "New Folder" in the array, then "New Folder" is returned.
If there is a folder with the name "New Folder" and there is no folder with the name "New Folder (2)", then "New Folder (2)" is returned ("New Folder (1)" is never used).
The N value of "New Folder (N)" should be incremented by 1 until a unique folder name is found.

For example, ```generateNewFolderName(["New Folder", "New Folder (3)", "New Folder (4)"])``` should return "New Folder (2)".

## Solution
I am proud to say that this was the first assignment i was able to finish without looking up anything :)
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Solution 4</title>
</head>
<body>
    <script>
        
        function generateNewFolderName(arr){
            if (arr.includes("New Folder")){
                let folderNumber = 2
                while (arr.includes(`New Folder (${folderNumber})`) == true){ // As long as there is a folder with the current folderNumber, increment the folderNumber until the folderNumber isnt in any of the array elements.
                    folderNumber += 1
                }
                return `New Folder (${folderNumber})`
            } else {
                return 'New Folder' // If 'New Folder' is not present, just return that.
            }
        }

        const folderName = generateNewFolderName(["New Folder", "New Folder (3)", "New Folder (4)"]) // -> New Folder (2)
        console.log(folderName)
    </script>
</body>
</html>
```
# Assignment 6
Complete this sequence of GIT commands (without specifying additional arguments). 
They create a feature branch named matrix, insert the file matrix.cpp, and merge the modifications back to the master branch:

My answers are incapsulated inside the `[]`'s

Make a feature branch:

  `git [ branch matrix ] matrix` [Source](https://www.atlassian.com/git/tutorials/using-branches/git-checkout#:~:text=When%20you%20want,git%20branch%20new_branch)

Switch to the feature branch:

  `git [ checkout ] matrix`

1. Insert file matrix.cpp into the local directory

2. Mark that file matrix.cpp has been inserted:

3. git add matrix.cpp Commit any changes:

4. git commit -m 'Added support for matrix'

Switch to the main branch:

  `git [ checkout ] master`

Join the feature and main branches:


  `git [ merge matrix ] matrix` [Source](https://www.atlassian.com/git/tutorials/using-branches/git-merge#:~:text=git%C2%A0checkout%C2%A0main-,git%C2%A0merge%C2%A0new%2Dfeature,-git%C2%A0branch%C2%A0%2Dd)
# Assignment 7
Implement the find_all_hobbyists function that takes a hobby, and an object consisting of peoples names mapped to their respective hobbies. The function should return a List containing the names of the people (in any order) that enjoy the hobby.

For example, the following code should display the name 'Chad'.

```PYTHON
hobbies = {"Steve": ['Fashion', 'Piano', 'Reading'], "Patty": ['Drama', 'Magic', 'Pets'],"Chad": ['Puzzles', 'Pets', 'Yoga']}

print(find_all_hobbyists('Yoga', hobbies));
    
```

Example start:

```PYTHON
def find_all_hobbyists(hobby, hobbies):
  return []

if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga']
    }
    
print(find_all_hobbyists('Yoga', hobbies));
```
## Solution
With python being my strongpoint, i was able to whip up a one liner for this one :)

```PYTHON
def find_all_hobbyists(hobby, hobbies):
    # Loop through hobbies and add every name whos hobby-list has the supplied hobby in it.
    return [ person for person in hobbies.keys() if hobby in hobbies[person] ]

if __name__ == "__main__":
    hobbies = { 
        "Steve": ['Fashion', 'Piano', 'Reading'],
        "Patty": ['Drama', 'Magic', 'Pets'],
        "Chad": ['Puzzles', 'Pets', 'Yoga'],
        "Nils": ['Programming', 'biking', 'Yoga'],
    }
    
print(find_all_hobbyists('Yoga', hobbies)); # -> ['Chad', 'Nils']
input() # Prevent the program from exiting right away when run on the console
```

# Conclusion
I genuinely found these cases challenging and fun, a lot of them had me thinking and looking up things I didn’t know before.
