var chart1,chart2,chart3,chart4;

$('#BarChart').ready(function(e){
    // e.preventdefault;
    $.ajax({
        type:'GET',
        url:"graph/",
        dataType:'json',
    }).done(function(data) {
        stackedbarchartgraph(data)    
})})

function stackedbarchartgraph(data) {
    var ctx = document.getElementById("BarChart").getContext('2d');
    chart1 = new Chart(ctx, {
        type: 'bar',
        data: {
           labels: data.columns, 
           datasets: []
        },
        options: {
           responsive: true,
           legend: {
              position: 'right', // place legend on the right side of chart
              
              onClick: function(e, legendItem) {
                var index = legendItem.datasetIndex;
                
                var ci = this.chart;
                var alreadyHidden = (ci.getDatasetMeta(index).hidden === null) ? false : ci.getDatasetMeta(index).hidden;
                var anyOthersAlreadyHidden = false;
                var allOthersHidden = true;
        
                ci.data.datasets.forEach(function(e, i) {
                  var meta = ci.getDatasetMeta(i);
        
                  if (i !== index) {
                    if (meta.hidden) {
                      anyOthersAlreadyHidden = true;
                    } else {
                      allOthersHidden = false;
                    }
                  }
                });
        
                if (alreadyHidden) {
                  ci.getDatasetMeta(index).hidden = null;
                } else {
                  ci.data.datasets.forEach(function(e, i) {
                    var meta = ci.getDatasetMeta(i);
        
                    if (i !== index) {
                      if (anyOthersAlreadyHidden && !allOthersHidden) {
                        meta.hidden = true;
                      } else {
                        meta.hidden = meta.hidden === null ? !meta.hidden : null;
                      }
                    } else {
                      meta.hidden = null;
                    }
                  });
                }
        
                ci.update();
              },
              
           },
           scales: {
              xAxes: [{
                 stacked: true, // this should be set to make the bars stacked
                 ticks: {
                    autoSkip: false,
                    maxRotation: 45,
                    minRotation: 45
                }
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
            backgroundColor: dynamicColors(),
            
        };
        for (value in data.data[i]) {
            newDataset.data.push(data.data[i][value]);
            
        }      
        chart1.config.data.datasets.push(newDataset);
    }
    chart1.update();
}

function dynamicColors() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgba(" + r + "," + g + "," + b + ", 1)";
}