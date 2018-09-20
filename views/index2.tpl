<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>json apis.is</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
	<div class="row">
		<section>
			<h2>Gengi gjaldmiðla frá apis.is.</h2>
			<ul>
				% for i in data['results']:
				<li>
					{{i['longName']}} - {{i['shortName']}} ISKR: {{i['value']}}
				</li>
				% end
			</ul>
		</section>
	</div>
	% include('fotur.tpl')
</body>
</html>