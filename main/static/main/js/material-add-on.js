$(document).ready(function(){

  $("#myInput").on("keyup", function() {
     var value = $(this).val().toLowerCase();
     $("#bob li" ).filter(function() {
       $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
     });
   });

  $('.collapsible').collapsible();
  $('.tabs').tabs();
  $('.datepicker').datepicker()
  $(".dropdown-trigger").dropdown();
  $('select').formSelect();
  $('.modal').modal();

 });


 document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
  });

  // Or with jQuery

    document.addEventListener('DOMContentLoaded', function() {
      var elems = document.querySelectorAll('.sidenav');
      var instances = M.Sidenav.init(elems, options);
    });

    // Initialize collapsible (uncomment the lines below if you use the dropdown variation)
    // var collapsibleElem = document.querySelector('.collapsible');
    // var collapsibleInstance = M.Collapsible.init(collapsibleElem, options);

    // Or with jQuery

    $(document).ready(function(){
      $('.sidenav').sidenav();
    });
          
  var instance = M.Sidenav.getInstance(elem);

    /* jQuery Method Calls
      You can still use the old jQuery plugin method calls.
      But you won't be able to access instance properties.

      $('.sidenav').sidenav('methodName');
      $('.sidenav').sidenav('methodName', paramName);
    */
