var myChartBar1;
$('#myChartBar1').ready(function(e){
  // e.preventdefault;
  $.ajax({
      type:'GET',
      url:"graph/",
      dataType:'json',
  }).done(function(data) {
    console.log(data)
  
    bar_graph(data,'myChartBar1')  
      
})
  function bar_graph(data, id) {
  var ctx = document.getElementById("myChartBar1").getContext('2d');
  myChartBar1 = new Chart(ctx, {
      type: 'bar',
      data: {
         labels: data.columns, 
         
         datasets: []
      },
      options: {
         responsive: true,
         legend: {
            
            display : false,
            

            
         },

         legendCallback: function(chart) { 
          var text = []; 
          text.push('<ul class="' + chart.id + '-legend">'); 
          for (var i = 0; i < chart.data.datasets.length; i++) { 
              text.push('<li><span style="background-color:' + chart.data.datasets[i].backgroundColor + ' " "   onclick="updateDataset(event,' + '\'' + i + '\'' + ')" ></span>'); 
              if (chart.data.datasets[i].label) { 
                  text.push(chart.data.datasets[i].label); 
              } 
              text.push('</li>'); 
          } 
          text.push('</ul>'); 
          return text.join(''); 
      },
         scales: {
            xAxes: [{
               stacked: true, // this should be set to make the bars stacked
            }],
            yAxes: [{
               stacked: true // this also..
            }]
         }
      }
   });
   
   for (i in data.index) {
      var newDataset = {
          label: data.index[i],
          data: [],
          backgroundColor: dynamicColors(i),
          
      };
      for (value in data.data[i]) {
          newDataset.data.push(data.data[i][value]);
          
      }      
      myChartBar1.config.data.datasets.push(newDataset);
  }

  myChartBar1.update(); 
 
   $("#legendbarchart").append(myChartBar1.generateLegend())

  
 
}
})

function dynamicColors(i) {
  return [
    'rgba(230,132,181, 1)',
    'rgba(233,199,130, 1)',
    'rgba(117,189,205, 1)',
    'rgba(151,110,73, 1)',
    'rgba(158,26,101, 1)',
    'rgba(126,238,231, 1)',
    'rgba(217,53,11, 1)',
    'rgba(140,156,48, 1)',
    'rgba(105,123,249, 1)',
    'rgba(157,66,195, 1)',
    'rgba(59,73,41, 1)',
    'rgba(155,33,210, 1)',
    'rgba(79,178,70, 1)',
    'rgba(184,81,104, 1)',
    'rgba(211,156,1, 1)',
    'rgba(170,168,2, 1)',
    'rgba(41,141,173, 1)',
    'rgba(177,46,44, 1)',
    'rgba(33,32,102, 1)',
    'rgba(204,122,46, 1)',
    'rgba(43,155,138, 1)',
    'rgba(11,117,161, 1)',
    'rgba(244,40,208, 1)',
    'rgba(65,46,138, 1)',
    'rgba(195,174,37, 1)',
    'rgba(233,76,52, 1)',
    'rgba(18,170,162, 1)',
    'rgba(103,184,212, 1)',
    'rgba(106,23,0, 1)',
    'rgba(105,7,173, 1)',
    'rgba(3,106,115, 1)',
    'rgba(19,227,24, 1)',
    'rgba(238,119,106, 1)',
    'rgba(163,57,17, 1)',
    'rgba(9,204,77, 1)',
    'rgba(75,186,54, 1)',
    'rgba(228,65,25, 1)',
    'rgba(87,60,226, 1)',
    'rgba(237,147,224, 1)',
    'rgba(158,2,119, 1)',
    'rgba(182,179,245, 1)',
    'rgba(147,78,11, 1)',
    'rgba(213,68,197, 1)',
    'rgba(147,149,234, 1)',
    'rgba(220,75,6, 1)',
    'rgba(136,56,167, 1)',
    'rgba(35,171,201, 1)',
    'rgba(105,205,241, 1)',
    'rgba(221,18,43, 1)',
    'rgba(41,62,151, 1)'][i]
   
}
var meta_all_hidden = false 
function updateDataset(e, legendItem) {
  var index = legendItem;
  var ci = myChartBar1;
  var meta = ci.getDatasetMeta(index);

  console.log(meta_all_hidden)
  // See controller.isDatasetVisible comment
  if (meta_all_hidden == false){
    console.log("inside if")
   for (i=0;i<ci.data.datasets.length;i++) {
    if (i!=index && meta_all_hidden == false){
      ci.data.datasets[i].hidden = true
    } else {
      ci.data.datasets[i].hidden = null
    }
   }
   meta_all_hidden = true
   console.log()
 
  } else {
    console.log("inside else")
    for (i=0;i<ci.data.datasets.length;i++) {
      if (i!=index && meta_all_hidden == true){
        ci.data.datasets[i].hidden = null
        
      } 
     }
     meta_all_hidden = false
  }
 
  for (i=0;i<ci.data.datasets.length;i++) {
  console.log(ci.data.datasets[i].hidden)
}
  
  ci.update();
}


// new graph start


var  myChartBar2;
var chartdata;
var labels;

$('#drillgraph').ready(function(e){
  $.ajax({
      type:'GET',
      url:"div/",
      dataType:'json',
  }).done(function(data) {
   
     bar_graph(data,'myChartBar2')
  })
})

function bar_graph(data,id) {
   labels = data.col;
   chartdata = data.value;
  var taluka = [data.staluka,data.ntaluka];
  var values = [data.svalues,data.nvalues]

  var ctx = document.getElementById(id).getContext('2d');
  myChartBar2 = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        data: chartdata,
        borderRadius: 5,
        backgroundColor: [
          'rgba(255, 60, 183, 0.8)',
          'rgba(54, 162, 235, 0.8)',
          'rgba(255, 206, 86, 0.8)',
          'rgba(75, 192, 192, 0.8)',
          'rgba(153, 102, 255, 0.8)',
          'rgba(255, 202, 70, 0.8)',
          'rgba(255, 226, 95, 0.8)',
          'rgba(255, 159, 150, 0.8)',
          'rgba(150, 255, 255, 0.8)',
          'rgba(252, 125, 25, 0.8)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 159, 64, 1)'
        ],
      
      }]
    },
    options: {
      legend: {
        
        display: false }, 
  
        onClick: function(e) {
          var bar = this.getElementAtEvent(e)[0];
          if (bar != undefined) {
              var index = bar._index;
              changechart(index)
              
          }
     },

      onHover: (event, chartElement) => {
     
        var target = event.native ? event.native.target : event.target;
        target.style.cursor = chartElement[0] ? 'pointer' : 'default';
    },
    plugins: {
     
       } ,
    
    responsive: true,
         responsive: true,
      scales: {
        xAxes:{
          grid: {
            display: false
          }
        },
        yAxes: {
            beginAtZero: true,
            grid: {
              display: false
            }  
        }
       
      },
      
    }
  });

  function changechart(index){
  if (myChartBar2.config.data.labels === labels ){
  myChartBar2.config.data.datasets[0].data = values[index];
  myChartBar2.config.data.labels = taluka[index];
 
  myChartBar2.update();

  }
}
}
function resetchart (){
  
  myChartBar2.config.data.datasets[0].data = chartdata;
  myChartBar2.config.data.labels = labels
  myChartBar2.update();
}


function remove_img(){
  $(".modal-body").html("");
}

function view_img(id) {

  
  $.ajax(
    {
        type:"GET",
        url: "/works_reports/img_view/"+13+"",
        datatype:'json',
        
        success: function(data)
         
        {if (data.length === 0 ) 
          {
            $("#pappu").append('<label>No Data Available</label>');
          
        }
          else{ 
          var iterator = 0

          var div1 = document.createElement("div")
          div1.className = "row " + String(0)
          console.log(div1)
            // console.log(div1)
            
           for (var j = 0; j<data.length;j++) {
            if(data[iterator][0] != null && data[iterator][1] != null ){
            var fl= data[iterator][0].split('.').pop();
            // console.log(fl)
            if( fl in ['jpg','JPG','PNG','png']){
              console.log(fl)
            }
            var div2 = document.createElement("div")
            div2.className = "col-3 ml-0 mt-2 pl-0"
          
            var img1 = document.createElement("img")
            img1.className="img-fluid"
            img1.src = 'http://115.124.114.20:8080/ZP_Dev/img/view/'+String(data[iterator][0])
            img1.width = "100"
            img1.height = "100"
            div2.appendChild(img1)
            div1.appendChild(div2)
            img1.setAttribute("class",'ml-2');
            img1.setAttribute("onclick",'showImage(this.src);');
            }
            iterator = iterator + 1
           }

              var element = document.getElementById("pappu");
              element.appendChild(div1);
          }
        }
    })
  }



function showImage(img){

    var modal = document.getElementById('myModal12');
    // var img = document.getElementById('img01');
    var modal1 = document.getElementById('myModal');
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    modal1.style.display="none";
    modal.style.display = "block";
  
    modalImg.src = img;
    console.log( modalImg.src)
    captionText.innerHTML = this.alt;
    }

function closs_img(){
    
    var modal = document.getElementById('myModal12');
    var modal1 = document.getElementById('myModal');
    modal.style.display = "none";
    modal1.style.display="block";

}