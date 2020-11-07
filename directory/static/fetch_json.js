function get_application_from_name (name) {
	$.get("https://opendata.hawaii.gov/api/3/action/datastore_search_sql",
		"sql=SELECT * from \"63c0030c-a8ff-419b-9139-990c475cc6e8\" WHERE \"name\" LIKE " +  "\'" + name + "\'",
		function(data) {

		}, "json");
	return tmp;
}

get_application_from_name("joe mamma");

