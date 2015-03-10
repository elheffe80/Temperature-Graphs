var data = [{
	"opacity":0.7,
	"error_x":{
		"color":"black",
		"copy_ystyle":true,
		"width":"2",
		"thickness":"1"
		},
		"uid":"f68cda",
		"ysrc":"elheffe:0:7Y3O6GBIQ8GTFLCGKJ2CGKTYPJT24UP4",
		"error_y":{
			"color":"black",
			"width":"2",
			"thickness":"1"
			},
		"xsrc":"elheffe:0:2NCKRR0YGGGSCPQPOXM6LC68FW9PBN2Y",
		"marker":{
			"opacity":1,
			"color":"rgba(0, 0, 0, 0)",
			"symbol":"square",
			"maxdisplayed":0,
			"line":{
				"color":"black",
				"width":0.8
				},
			"size":6
			},
			"mode":"markers",
			"line":{
				"color":"black",
				"width":1,
				"dash":"solid"
			},
			"fill":"none",
			"type":"scatter",
			"name":"MB Temp C"
		},
		{
			"opacity":0.7,
			"error_x":{
				"color":"black",
				"copy_ystyle":true,
				"width":"2",
				"thickness":"1"
				},
			"uid":"288244",
			"ysrc":"elheffe:0:AQYKY8NCK02K88A0UPL9JS0248TI100L",
			"error_y":{
				"color":"black",
				"width":"2",
				"thickness":"1"
				},
			"xsrc":"elheffe:0:2NCKRR0YGGGSCPQPOXM6LC68FW9PBN2Y",
			"marker":{
				"opacity":1,
				"color":"rgba(0, 0, 0, 0)",
				"symbol":"diamond",
				"maxdisplayed":0,
				"line":{
					"color":"black",
					"width":0.8
					},
				"size":6
				},
			"mode":"markers",
			"line":{
				"color":"black",
				"width":1,
				"dash":"solid"
				},
			"fill":"none",
			"type":"scatter",
			"name":"Outside Temp C"
			}
			];
var layout = {
	"hidesources":false,
	"autosize":true,
	"yaxis":{
		"domain":[],
		"showticklabels":true,
		"showexponent":"all",
		"titlefont":{
			"color":"black",
			"family":"\"Courier New\", monospace",
			"size":10
			},
		"linecolor":"rgba(152, 0, 0, 0.5)",
		"mirror":false,
		"autotick":true,
		"rangemode":"normal",
		"autorange":true,
		"nticks":5,
		"linewidth":1.5,
		"ticks":"",
		"showgrid":true,
		"zeroline":true,
		"gridcolor":"rgba(31, 119, 180, 0.25)",
		"type":"linear",
		"zerolinewidth":1,
		"ticklen":6,
		"showline":true,
		"tickfont":{
			"color":"black",
			"family":"\"Courier New\", monospace",
			"size":8
			},
		"tick0":0,
		"tickangle":"auto",
		"gridwidth":1,
		"dtick":1,
		"zerolinecolor":"#444",
		"range":[10.962646566164153,31.237353433835846],
		"tickcolor":"rgba(0, 0, 0, 0)",
		"exponentformat":"B"
	},
	"paper_bgcolor":"white",
	"plot_bgcolor":"white",
	"dragmode":"zoom",
	"showlegend":true,
	"separators":".,",
	"height":520,
	"width":735,
	"bargap":0.2,
	"titlefont":{
		"color":"black",
		"family":"\"Courier New\", monospace",
		"size":11
		},
	"xaxis":{
		"domain":[],
		"showticklabels":true,
		"gridcolor":"rgba(31, 119, 180, 0.25)",
		"linecolor":"rgba(152, 0, 0, 0.5)",
		"mirror":false,
		"autotick":true,
		"rangemode":"normal",
		"autorange":true,
		"nticks":5,
		"linewidth":1.5,
		"ticks":"inside",
		"showgrid":true,
		"zeroline":true,
		"type":"date",
		"zerolinewidth":1,
		"ticklen":6,
		"titlefont":{
			"color":"black",
			"family":"\"Courier New\", monospace",
			"size":10
			},
		"showline":true,
		"tickfont":{
			"color":"black",
			"family":"\"Courier New\", monospace",
			"size":8
			},
		"tick0":0,
		"tickangle":"auto",
		"gridwidth":1,
		"dtick":1,
		"zerolinecolor":"#444",
		"range":[1416823936240.196,1416963382759.804],
		"tickcolor":"rgba(0, 0, 0, 0)"
		},
	"hovermode":"x",
	"font":{
		"color":"#444",
		"family":"\"Courier New\", monospace",
		"size":10
		},
	"margin":{},
	"legend":{
		"bordercolor":"black",
		"traceorder":"normal",
		"yref":"paper",
		"bgcolor":"white",
		"xref":"paper",
		"borderwidth":0,
		"y":1,
		"x":0.02,
		"font":{
			"color":"#444",
			"family":"\"Open sans\", verdana, arial, sans-serif",
			"size":12
			}
		}
	};
Plotly.plot(Tabs.get(), data, layout);