const apiKey = '2d058c4a';

const searchBtn = document.getElementById('search-btn');
const searchBar = document.getElementById('search-bar');
const movieResults = document.getElementById('movie-results');

function fetchMovies(query) {
    fetch(`https://www.omdbapi.com/?s=${query}&apikey=${apiKey}`)
    .then(response => response.json())  
    .then(data => {
        if (data.Response === "True") {
            displayMovies(data.Search);
        } else {
            movieResults.innerHTML = `<p>No movies found. Please try again.</p>`;
        }
    })
    .catch(error => {
        console.log("Error fetching data:", error);
        movieResults.innerHTML = `<p>Error fetching movies. Please try again later.</p>`;
    });
}

function displayMovies(movies) {
    movieResults.innerHTML = '';  

    movies.forEach(movie => {
        const movieCard = document.createElement('div');
        movieCard.classList.add('movie-card');
        movieCard.innerHTML = `
            <img src="${movie.Poster}" alt="${movie.Title}">
            <h3>${movie.Title}</h3>
            <p><strong>Year:</strong> ${movie.Year}</p>
            <button class="details-btn">Show Details</button>
            <div class="movie-details" id="details-${movie.imdbID}">
                
            </div>
        `;

        movieResults.appendChild(movieCard);

       
        const detailsBtn = movieCard.querySelector('.details-btn');
        detailsBtn.addEventListener('click', function() {
            const detailsSection = movieCard.querySelector('.movie-details');
            fetchMovieDetails(movie.imdbID, detailsSection);
        });
    });
}


function fetchMovieDetails(imdbID, detailsSection) {
    fetch(`https://www.omdbapi.com/?i=${imdbID}&apikey=${apiKey}`)
    .then(response => response.json()) 
    .then(movie => {
        detailsSection.innerHTML = `
            <p><strong>Plot:</strong> ${movie.Plot}</p>
            <p><strong>Director:</strong> ${movie.Director}</p>
            <p><strong>Cast:</strong> ${movie.Actors}</p>
            <p><strong>Genre:</strong> ${movie.Genre}</p>
            <p><strong>IMDb Rating:</strong> ${movie.imdbRating}</p>
        `;
        detailsSection.style.display = 'block'; 
    })
    .catch(error => {
        console.log("Error fetching details:", error);
        detailsSection.innerHTML = `<p>Error fetching details. Please try again later.</p>`;
    });
}

 searchBtn.addEventListener('click', function() {
    const query = searchBar.value.trim();
    if (query) {
        fetchMovies(query);
    } else {
        alert("Please enter a movie title!");
    }
});

searchBar.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        searchBtn.click();
    }
});
