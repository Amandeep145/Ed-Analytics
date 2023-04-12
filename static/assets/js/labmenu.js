$(document).ready(function(e){
    
    $.ajax({
        type:'GET',
        url:$("#Url").attr("data-url"),
        dataType:'json',
    }).done(function(response) {
        var data = eval(response)
        console.log(data)
        for (let i = 0;i < data.length; i++){
            
            if (isNaN(data[i]['menu_parent_id'])){
                var li = document.createElement('li');
                li.setAttribute("class","has_sub")
                
                var aone = document.createElement('a');
                aone.href = 'javascript:void(0)';
                aone.setAttribute("id",data[i]['id']+'atag');
                var id = aone.id
                aone.onclick= (function(id) {return function() {
                    myFunction(id)
                };})(id);

                // class="metismenu list-unstyled"

                // var ione = document.createElement('i');
                // ione.setAttribute("class","fa fa-home");
                // aone.appendChild(ione);
                var ione = document.createElement('i');
                ione.setAttribute("class",data[i]["iconn"]);
                ione.setAttribute("style", "color:white;");
                aone.appendChild(ione);
                console.log(ione)

                var spanone = document.createElement('span');
                spanone.setAttribute("style", "color:white;");
                var text = document.createTextNode(data[i]['menuname']); 
                spanone.appendChild(text);
                aone.appendChild(spanone);

                var spantwo = document.createElement('span');
                spantwo.setAttribute("class","pull-right");

                var itwo = document.createElement('i');
                itwo.setAttribute("class","fa fa-angle-down");
                itwo.setAttribute("id",data[i]['id'].toString()+'i');
                spantwo.appendChild(itwo);
                aone.appendChild(spantwo);
                li.appendChild(aone);
                
                var ul = document.createElement('ul')
                ul.setAttribute('style',"display: none;")
                var litwo = document.createElement('li')
                litwo.setAttribute("class","has_sub")
                litwo.setAttribute("id",data[i]['id'])
                ul.appendChild(litwo)
                ul.setAttribute('id',data[i]['id']+'atagchange')
                
                li.appendChild(ul)
                document.getElementById("listlab").appendChild(li);
                
            } else if(isNaN(data[i]['menu_parent_id'])==false && data[i]['menuurl'] == "#"){
                var li = document.createElement('li');
                li.setAttribute("class","has_sub")
                

                var aone = document.createElement('a');
                aone.href = 'javascript:void(0)';
                aone.setAttribute("id",data[i]['id']+'atag');
                var id = aone.id
                aone.onclick= (function(id) {return function() {
                    myFunction(id)
                };})(id);

                var ione = document.createElement('i');
                ione.setAttribute("class",data[i]["iconn"]);
                aone.appendChild(ione);
                console.log(ione)

                var spanone = document.createElement('span');
                var text = document.createTextNode(data[i]['menuname']); 
                spanone.appendChild(text);
                aone.appendChild(spanone);

                var spantwo = document.createElement('span');
                spantwo.setAttribute("class","pull-right");
               

                var itwo = document.createElement('i');
                itwo.setAttribute("class","fa fa-angle-down");
                itwo.setAttribute("backgroundColor", "red");
                
                spantwo.appendChild(itwo);
                aone.appendChild(spantwo);
                li.appendChild(aone);
                
                var ul = document.createElement('ul')
                ul.setAttribute('style',"display: none;")
                var litwo = document.createElement('li')
                litwo.setAttribute("class","has_sub")
                litwo.setAttribute("id",data[i]['id'])
                ul.appendChild(litwo)
                ul.setAttribute('id',data[i]['id']+'atagchange')
                
                li.appendChild(ul)
                document.getElementById(data[i]['menu_parent_id']).appendChild(li);
                        };

            if (isNaN(data[i]['menu_parent_id'])==false && data[i]['menuurl'] != "#"){
                var li = document.createElement("li");
                var anchor = document.createElement("a");
                var span = document.createElement("span");
                var text = document.createTextNode(data[i]['menuname']);
                
                span.appendChild(text);
                anchor.appendChild(span);
                anchor.href = data[i]['menuurl'],
                li.appendChild(anchor);
                li.setAttribute("id",data[i]['id'])
                
                document.getElementById(data[i]['menu_parent_id']).appendChild(li);
            }
            
        }
    })
})

// document.getElementsByClassName("fa fa-angle-down").onclick = function() {myFunction()};
// var itag, i
// itag = document.getElementsByClassName("fa fa-angle-down")
// console.log(Object.keys(itag))
// for (i = 0;i <itag.length; i++){
//     console.log(itag[i])
//     itag[i].onclick = function() {myFunction(itag[i].id)};
// }
// var itag, i
// itag = document.getElementsByClassName("fa fa-angle-down")
// console.log(itag)
// for (i = 0;i <itag.length; i++){
//     console.log(itag[i])
//     itag[i].onclick = function() {myFunction(itag[i].id)};
// }


function myFunction(id) {
    targetid = id+'change';
    ul = document.getElementById(targetid).style.display
    if (ul == "block") {
        document.getElementById(targetid).style.display = "none";
    } else {
        document.getElementById(targetid).style.display = "block";
    }
  }

function loadmaster(data) {
    
}

function loadchild(data) {
    
}