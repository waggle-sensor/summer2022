# Tutorial Example: Publish Hello World

You can run this example as follows:

```sh
pip3 install -r requirements.txt
python3 main.py
```

After running `main.py`, you can view recent data using:

```sh
curl -H 'Content-Type: application/json' https://data.sagecontinuum.org/api/v1/query -d '
{
	"start": "-5m",
	"filter": {
		"name": "tutorial.hello_world"
	}
}
'
```

You can learn more about [accessing data](https://docs.sagecontinuum.org/docs/tutorials/accessing-data) in the [Sage docs](https://docs.sagecontinuum.org).
