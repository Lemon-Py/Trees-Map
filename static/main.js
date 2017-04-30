var my_map = L.map('full-map', {
			center: [20.0, 5.0],
			minZoom: 2,
			zoom: 2
});
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
	subdomains: ['a','b','c']
}).addTo(my_map);