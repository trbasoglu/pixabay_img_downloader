# Pixabay file downloader

It downloads images with given config. Config includes 3 value.
```
{
    "API-KEY":"INSERT_APIKEY-HERE",
    "Keywords":["landscape","road","city"],
    "pageNumber":10
}
```

You can use any keyword and page number. You can use different config files. If config file name is different than ``config.json``, You must give it's path as first paramater.

```
python pixabay_image_downloade.py
```

or

```
python pixabay_image_downloade.py config2.json
```

* Api key is can be taken [here](https://pixabay.com/tr/service/about/api/)
* Detailed documentation of api [here](https://pixabay.com/api/docs/).