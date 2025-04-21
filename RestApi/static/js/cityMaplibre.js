$(document).ready(function () {

    const map = new maplibregl.Map({
        container: 'map',
        style: 'https://demotiles.maplibre.org/style.json', // URL to your MapLibre style
        center: [0, 0], // Starting position [lng, lat]
        zoom: 2 // Starting zoom level
    });

    map.addControl(new maplibregl.NavigationControl());

    // API call
    $.ajax({
        url: "/api/city/",
        method: "GET",
        success: function (data) {
        data.forEach(city => {
            const lat = city.location.coordinates[1];
            const lng = city.location.coordinates[0];

            const marker = new maplibregl.Marker()
            .setLngLat([lng, lat])
            .addTo(map);

            marker.setPopup(new maplibregl.Popup({ offset: 25 }) // add popups
            .setHTML(`<strong>${city.name}</strong><br>Population: ${city.population}`))
            .addTo(map);

            marker.getElement().addEventListener('click', function () {
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