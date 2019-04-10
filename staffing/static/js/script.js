(function($) {
  $(function() {
    // Plugin initialization
    $("select")
      .not(".disabled")
      .formSelect();
  });
})(jQuery);

$(function() {
  $("#id_date").datepicker({
    format: "dd/mm/yyyy"
  });
});
