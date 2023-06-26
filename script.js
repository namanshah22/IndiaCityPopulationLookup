$(document).ready(function() {
  $("#city").autocomplete({
      source: function(request, response) {
          $.ajax({
              url: "fetch_cities.php",
              type: "POST",
              data: { term: request.term },
              dataType: "json",
              success: function(data) {
                  response(data);
              }
          });
      },
      select: function(event, ui) {
          $("#cityInfo").html(
              "Rank: " + ui.item.rank + "<br>" +
              "City Population (2011): " + ui.item.population_2011 + "<br>" +
              "City Population (2001): " + ui.item.population_2001 + "<br>" +
              "State or Union Territory: " + ui.item.state_or_union_territory
          );
      }
  });
});

  