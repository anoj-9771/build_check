let fs = require('fs');

let content = fs.readFileSync('videodata.json', 'utf-8');

let data = JSON.parse(content);
// console.log(data);

data.categories.forEach(function(element){
    console.log(element.categoryName);
})