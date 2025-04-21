$(document).ready(function () {
  const map = L.map('map').setView([0, 0], 2);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  // API call
  $.ajax({
    url: "/api/city/",
    method: "GET",
    success: function (data) {
      data.forEach(city => {
        const lat = city.location.coordinates[1];
        const lng = city.location.coordinates[0];

        const marker = L.marker([lat, lng]).addTo(map);
        marker.bindPopup(`<strong>${city.name}</strong><br>Population: ${city.population}`);

        marker.on('click', function () {
          $('#city-info').html(`
            <h3>${city.name}</h3>
            <p>Population: ${city.population}</p>
            <img src="${city.image}" alt="${city.name}" style="max-width: 100%;">
          `);
        });
      });
    },
    error: function (xhr, status, error) {
      console.error("Erreur API:", error);
    }
  });
});
