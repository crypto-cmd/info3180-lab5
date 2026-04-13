<template>
  <div class="container mt-5">
    <h2 class="mb-4">Movies</h2>
    
    <div class="row row-cols-1 row-cols-md-2 g-4">
      
      <div v-for="movie in movies" :key="movie.id" class="col">
        
        <div class="card h-100 shadow-sm mb-3">
          <div class="row g-0 h-100">
            
            <div class="col-md-4">
              <img :src="movie.poster" class="img-fluid rounded-start h-100" alt="Movie Poster" style="object-fit: cover; width: 100%;">
            </div>
            
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title fw-bold">{{ movie.title }}</h5>
                <p class="card-text">{{ movie.description }}</p>
              </div>
            </div>
            
          </div>
        </div>

      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);
let loading = ref(true);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies;
      loading.value = false;
    })
    .catch((error) => {
      console.log(error);
      loading.value = false;
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
/* Add any component specific styles here */
</style>