$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const movieList = data.results;
  $.each(movieList, (idx, val) => {
    $('UL#list_movies').append('<li>' + val.title + '</li>');
  });
});
