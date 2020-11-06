function get_json () {
	var data = {
		resource_id: '9468a555-8d1f-42fb-b1a9-c3ae0d5c756d', // the resource id
		limit: 5, // get 5 results
		q: 'jones' // query for 'jones'
	};
	$.ajax({
		url: 'https://opendata.hawaii.gov/api/3/action/datastore_search',
		data: data,
		dataType: 'jsonp',
		success: function(data) {
			alert('Total results found: ' + data.result.total)
		}
	});
}

get_json();

