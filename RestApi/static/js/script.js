$(document).ready(function() {
    $.ajax({
        url: '/api/team',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            const container = $('#card-grid');
            container.empty(); // Clear existing content

            data.forEach((team) => {
                const card = `
                 <div class="card" style="width: 18rem;">
                    <img src="${team.image}" alt="${team.name}">
                    <div class="card-body">
                        <p class="card-text">${team.name}</p>
                    </div>
                 </div>`;
                container.append(card);
            });
        },
        error: function (error) {
            console.error('Error fetching team data:', error);
        }
    });
});