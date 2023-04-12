function module_list(){
    $('#submenu').append('<option  value="">Select</option>');
    id = $("#menu_master_id").val();
    $.ajax(
      {
         type:"GET",
          url: "",
          data:{
            mainmenu: id, 
          },
          success: function( data ) 
        
         {  
           
              data.forEach(a => {
                var opt = document.createElement("option"); 
                console.log(opt)       
                opt.text = a[0];

                opt.value = a[1];
                document.getElementById('submenu').options.add(opt);
              });   
          }
      }) 
  }
  





  function sub_list(){
    $('#submenu').empty().append('<option disabled value="">Select</option>');
    id = $("#menu_master_id").val();
    $.ajax(
      {
         type:"GET",
          url: "",
          data:{
            mainmenu: id, 
          },
          success: function( data ) 
          

          
          {
            
            // console.log(aa)
            // console.log(jj)
              data.a.forEach(a => {
                var opt = document.createElement("option"); 
                console.log(opt)       
                opt.text = a[0];

                opt.value = a[1];
                document.getElementById('submenu').options.add(opt);
              });   
              // // var aa = data.a;
              // var jj = data.hjj;
              // // console.log(jj)
              // jj.forEach(j => {
              //   var same = j[0];
              //   // console.log(same)
              //   var optt = document.getElementById('submenu')
              //   console.log(optt)
              //   if (same = optt.text){
              //     var att = document.setAttribute('selected')
              //     document.getElementById('submenu').options.add(att);
              //   }
                
              // })
          }
      }) 
  }
  

