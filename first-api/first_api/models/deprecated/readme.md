# Deprecated? 

These are just some pydantic models generated from the available OpenAPI specification, detected with this **awesome** Chrome [extension](https://github.com/AndrewWalsh/openapi-devtools). 

The models themselves are generated by pydantic's [official CLI tool](https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/) (which is neat just like the rest of pydantic). 
You can use it to generate models directly from: 

+ *JSON* or *YAML* data, which then gets turned first into *JSON Schema* 
+ *JSON Schema* itself, of course
+ *OpenAPI 3* specification, either in YAML or JSON. 

I generated the models from the OpenAPI specifications I retrieved by calling the OpenWeatherMap API, but imho they're practically way too complex to use for any basic use case. 
I just left them here just in case. 

The *Weather 2.5* API call is somehow a hidden entrypoint for retrieving a weather report from longitude and latitude, it works with the free tier. I could not find it in the docs, which only mentions the *Onecall 3.0* api, and it requires an extra "pay as you need" type of subscription. 

The *Geocoding 1.0* api is used to retrieve longitude and latitude from a city (and state). 