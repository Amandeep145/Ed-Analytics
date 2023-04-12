const list = document.querySelectorAll('ul li')


// add active list to sidebar links list.
list.forEach( li => {
  li.addEventListener('click', e =>{
    list.forEach( li => {
      li.classList.remove('active')
    })
    e.currentTarget.classList.add('active')
  })
})

// chart 1
var xArray1 = ["Italy", "France", "Spain", "USA", "Argentina"];
var yArray1 = [55, 49, 44, 24, 15];

var layout1 = {title:"World Wide mineral water Production"};

var data1 = [{labels:xArray1, values:yArray1, type:"pie"}];

Plotly.newPlot("chart-1", data1, layout1);

// chart 2

var xArray2 = ["Italy","France","Spain","USA","Argentina"];
var yArray2 = [55, 49, 44, 24, 15];

var data2 = [{
  x: xArray2,
  y: yArray2,
  type: "bar"  }];
var layout2 = {title:"World Wide mineral water Production"};

Plotly.newPlot("chart-2", data2, layout2);


// chart 3
var xArray3 = [55, 49, 44, 24, 15];
var yArray3 = ["Italy","France","Spain","USA","Argentina"];

var data3 = [{
  x: xArray3,
  y: yArray3,
  type: "bar",
  orientation: "h"
}];

var layout3 = {title:"World Wide mineral water Production"};

Plotly.newPlot("chart-3", data3, layout3);
// chart 4

var xArray4 = [50,60,70,80,90,100,110,120,130,140,150];
var yArray4 = [7,8,8,9,9,9,10,11,14,14,15];

// Define Data
var data4 = [{
  x: xArray4,
  y: yArray4,
  mode:"markers",
  type:"scatter"
}];

// Define Layout
var layout4 = {
  xaxis: {range: [40, 160], title: "Square Meters"},
  yaxis: {range: [5, 16], title: "Price in Millions"},
  title: "House Prices vs. Size"
};

Plotly.newPlot("chart-4", data4, layout4);