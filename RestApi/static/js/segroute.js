$(document).ready(function () {
  const map = new maplibregl.Map({
    container: 'map',
    style: 'https://demotiles.maplibre.org/style.json',
    center: [0, 0],
    zoom: 2
  });

  // Afficher les routes
  $.getJSON("/api/roads/", function (roadData) {
    map.on('load', () => {
      map.addSource('roads', {
        type: 'geojson',
        data: roadData
      });

      map.addLayer({
        id: 'road-layer',
        type: 'line',
        source: 'roads',
        paint: {
          'line-color': '#0000ff',
          'line-width': 4
        }
      });

      // Ensuite, charger les segments
      $.getJSON("/api/segments/", function (segmentData) {
        map.addSource('road_segments', {
          type: 'geojson',
          data: segmentData
        });

        map.addLayer({
          id: 'segment-layer',
          type: 'line',
          source: 'road_segments',
          paint: {
            'line-color': [
              'match',
              ['get', 'status'],
              'good', '#00ff00',
              'works', '#ffa500',
              'slow', '#ff0000',
              '#000000'  // défaut
            ],
            'line-width': 3,
            'line-dasharray': [2, 2]
          }
        });
      });
    });
  });
});